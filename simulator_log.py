import os

import pandas as pd

from blockchain_data_structures import Block
from blockchain_node import Node


class LogRecord:
    def __init__(self, timestamp, blocks_counter, self_blocks_counter,
                 forks_counter):
        self.timestamp = timestamp
        self.blocks_counter = blocks_counter
        self.self_blocks_counter = self_blocks_counter
        self.forks_counter = forks_counter

    @staticmethod
    def columns_names():
        return ["Timestamp", "Blocks Count", "Self Blocks", "Forks Count"]

    def get_data_as_tuple(self):
        return self.timestamp, self.blocks_counter, self.self_blocks_counter, self.forks_counter


class NodeData:
    def __init__(self):
        self.log = []
        self.first_block_timestamp = None
        self.first_foreign_block_timestamp = None
        self.first_foreign_block_index = None

    @staticmethod
    def singletons_names():
        return ["First Block Timestamp", "First Foreign Block Timestamp",
                "First Foreign Block Index"]

    def add_record(self, log_record: LogRecord):
        self.log.append(log_record)

    def get_log(self):
        return self.log

    def set_first_block_timestamp(self, b):
        self.first_block_timestamp = b.get_timestamp()

    def set_first_foreign_block_data(self, b):
        self.first_foreign_block_timestamp = b.get_timestamp()
        self.first_foreign_block_index = b.get_index()

    def get_singletons(self):
        return self.first_block_timestamp, self.first_foreign_block_timestamp, \
               self.first_foreign_block_index


class SimulatorLog:
    def __init__(self, num_nodes, experiment_name, setup_description):
        self.num_nodes = num_nodes
        self.experiment_name = experiment_name
        # list of rows for each node
        self.nodes_log_dict = {i: NodeData() for i in range(num_nodes)}
        self.data_frames_dict = {i: None for i in range(num_nodes)}
        self.singletons_data_frames_dict = {i: None for i in range(num_nodes)}
        self.root_dir_name = "results"
        self.setup_description = setup_description

    def snapshot_blockchains(self, nodes):
        for node in nodes:
            node_log = self.nodes_log_dict[node.get_id()]  # type: NodeData
            b = node.get_block_chain()  # type: Block
            self_blocks_count = 0
            forks_count = -1  # To eliminate genesis block's fork
            while b.get_index() != 0:
                if b.get_forks_counter() > 0:
                    forks_count += b.get_forks_counter()
                if b.get_owner_id() == node.get_id():
                    self_blocks_count += 1
                else:
                    node_log.set_first_foreign_block_data(b)
                node_log.set_first_block_timestamp(b)
                b = b.get_prev()
            assert (b.get_index() == 0 and b.get_forks_counter() >= 0)
            forks_count += b.get_forks_counter()
            b = node.get_block_chain()
            node_log.add_record(LogRecord(b.get_timestamp(), b.get_index(),
                                          self_blocks_count, forks_count))

    # TODO: split save data to several methods
    def save_data(self, verbose=False):
        root_dir_name = self.root_dir_name
        if not os.path.exists(root_dir_name):
            os.makedirs(root_dir_name)
        experiment_dir_path = os.path.join(root_dir_name, self.experiment_name)
        assert not os.path.exists(experiment_dir_path)
        os.makedirs(experiment_dir_path)
        setup_description_file_path = os.path.join(experiment_dir_path,
                                                   "setup_description")
        if not os.path.exists(setup_description_file_path):
            with open(setup_description_file_path, 'w') as setup_description:
                setup_description.write(self.setup_description)
        if verbose:
            print(self.setup_description)

        for i in range(self.num_nodes):
            node_log_file_path = os.path.join(experiment_dir_path, "node"
                                              + str(i) + "_log")
            singletons_file_path = os.path.join(experiment_dir_path, "node"
                                                + str(i) + "_singletons")
            node_data = self.nodes_log_dict[i]  # type: NodeData
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

    def load_data(self, verbose=False):
        root_dir_name = self.root_dir_name
        experiment_dir_path = os.path.join(root_dir_name, self.experiment_name)
        assert os.path.exists(experiment_dir_path)
        for i in range(self.num_nodes):
            node_data_file_path = os.path.join(experiment_dir_path, "node"
                                               + str(i) + "_log")
            singletons_file_path = os.path.join(experiment_dir_path, "node"
                                                + str(i) + "_singletons")
            df = pd.read_pickle(node_data_file_path)
            df_singletons = pd.read_pickle(singletons_file_path)
            self.data_frames_dict[i] = df
            self.singletons_data_frames_dict[i] = df_singletons
            if verbose is True:
                print(node_data_file_path)
                print(df)
                print(singletons_file_path)
                print(df_singletons)
