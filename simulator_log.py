import os

import pandas as pd

from blockchain_data_structures import Block
from blockchain_node import Node


class LogRecord:
    def __init__(self, timestamp, blocks_counter, self_blocks_counter):
        self.timestamp = timestamp
        self.blocks_counter = blocks_counter
        self.self_blocks_counter = self_blocks_counter

    @staticmethod
    def columns_names():
        return ["Timestamp", "Blocks Count", "Self Blocks"]

    def get_data_as_tuple(self):
        return self.timestamp, self.blocks_counter, self.self_blocks_counter


class NodeData:
    def __init__(self):
        self.log = []
        self.first_block_timestamp = None
        self.first_foreign_block_timestamp = None

    @staticmethod
    def singletons_names():
        return ["First Block Timestamp", "First Foreign Block Timestamp"]

    def add_record(self, log_record: LogRecord):
        self.log.append(log_record)

    def get_log(self):
        return self.log

    def set_first_block_timestamp(self, b):
        self.first_block_timestamp = b.get_timestamp()

    def set_first_foreign_block_timestamp(self, b):
        self.first_foreign_block_timestamp = b.get_timestamp()

    def get_singletons(self):
        return self.first_block_timestamp, self.first_foreign_block_timestamp


class SimulatorLog:
    def __init__(self, num_nodes, experiment_name):
        self.num_nodes = num_nodes
        self.experiment_name = experiment_name
        # list of rows for each node
        self.node_logs_dict = {i: NodeData() for i in range(num_nodes)}
        self.root_dir_name = "results"

    def snapshot_blockchains(self, nodes):
        for i in range(self.num_nodes):
            node = nodes[i]  # type: Node
            node_log = self.node_logs_dict[node.get_id()]  # type: NodeData
            b = node.get_block_chain()  # type: Block
            timestamp = b.get_timestamp()
            blocks_count = 0
            self_blocks_count = 0
            while b.get_index() != 0:
                if b.get_owner_id() == node.get_id():
                    self_blocks_count += 1
                else:
                    node_log.set_first_foreign_block_timestamp(b)
                blocks_count += 1
                node_log.set_first_block_timestamp(b)
                b = b.get_prev()
            node_log.add_record(LogRecord(timestamp, blocks_count,
                                          self_blocks_count))

    def save_data(self, verbose=False):
        root_dir_name = self.root_dir_name
        if not os.path.exists(root_dir_name):
            os.makedirs(root_dir_name)
        experiment_dir_path = os.path.join(root_dir_name, self.experiment_name)
        assert not os.path.exists(experiment_dir_path)
        os.makedirs(experiment_dir_path)
        for i in range(self.num_nodes):
            node_log_file_path = os.path.join(experiment_dir_path, "node"
                                               + str(i) + "_log")
            singletons_file_path = os.path.join(experiment_dir_path, "node"
                                                + str(i) + "_singletons")
            node_data = self.node_logs_dict[i]  # type: NodeData
            df = pd.DataFrame(data=map(LogRecord.get_data_as_tuple,
                                       node_data.get_log()),
                              columns=LogRecord.columns_names())
            df_singletons = pd.DataFrame([node_data.get_singletons()],
                                         columns=NodeData.singletons_names())
            if verbose:
                print(node_log_file_path)
                print(df)
                print(singletons_file_path)
                print(df_singletons)
            df.to_pickle(path=node_log_file_path)
            df_singletons.to_pickle(path=singletons_file_path)

    def load_data(self):
        # todo: fix load data
        root_dir_name = self.root_dir_name
        experiment_dir_path = os.path.join(root_dir_name, self.experiment_name)
        for i in range(self.num_nodes):
            node_data_file_path = os.path.join(experiment_dir_path, "node"
                                               + str(i) + "_log")
            self.node_logs_dict = {i: pd.read_pickle(node_data_file_path)
                                   for i in range(self.num_nodes)}
