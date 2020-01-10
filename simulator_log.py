import os
import pickle

import pandas as pd

import my_globals

from blockchain_data_structures import Block
from blockchain_node import Node

# Constant strings
from system import System

ROOT_DIR = "results"
SETUP_FILE = "setup_description"
SYSTEM_PICKLE = "system_pickle"
LOG_FILE = "log_{}.csv"
SINGLETONS_FILE = "singletons_{}.csv"
NODE_DIR = "node_{}"
SYSTEM_RUN_FILE = "system_run_data.csv"


# Class for recording blockchain's data
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
    def __init__(self, node: Node):
        self.log = []  # list of LogRecords
        self.node = node
        self.blocks_count = 0
        self.self_blocks = 0
        self.forks_count = 0
        self.first_block_timestamp = -1  # convenient for aggregations

    @staticmethod
    def singletons_names():
        return ["Blocks Count", "Self Blocks", "Forks Count", "First Block Timestamp", "First Foreign Block Timestamp",
                "First Foreign Block Index"]

    def get_singletons(self):
        return self.blocks_count, self.self_blocks, self.forks_count, self.first_block_timestamp, \
               self.node.get_ffbi_timestamp(), self.node.get_ffbi()

    def add_record(self, log_record: LogRecord):
        self.log.append(log_record)

    def get_log(self):
        return self.log

    def set_first_block_timestamp(self, b):
        self.first_block_timestamp = b.get_timestamp()

    def get_first_foreign_block_index(self):
        return self.node.get_ffbi()

    def set_forks_count(self, forks_count):
        self.forks_count = forks_count

    def set_blocks_count(self, blocks_count):
        self.blocks_count = blocks_count

    def set_self_blocks_count(self, self_blocks_count):
        self.self_blocks = self_blocks_count

    def get_self_blocks(self):
        return self.self_blocks

    def get_blocks_count(self):
        return self.blocks_count


class SimulatorLog:
    def __init__(self, system: System, experiment_name, setup_description):
        self.num_nodes = system.get_num_nodes()
        self.experiment_name = experiment_name
        # list of rows for each node
        self.nodes_data_dict = {i: NodeData(node) for i, node in enumerate(system.get_nodes())}
        self.data_frames_dict = {i: None for i in range(self.num_nodes)}
        self.singletons_data_frames_dict = {i: None for i in range(self.num_nodes)}
        self.setup_description = setup_description
        self.global_forks_count = 0

    def snapshot_blockchains(self, nodes):
        for node in nodes:
            node_data = self.nodes_data_dict[node.get_id()]  # type: NodeData
            b = node.get_block_chain()  # type: Block
            self_blocks_count = 0
            forks_count = 0
            while b.get_index() != 0:
                forks_count, self_blocks_count = self._snapshot_block_aux(b, node, forks_count,
                                                                          self_blocks_count, node_data)
                b = b.get_prev()
            assert (b.get_index() == 0 and b.get_forks_counter() >= 0)
            forks_count += b.get_forks_counter()
            b = node.get_block_chain()
            node_data.set_forks_count(forks_count)
            node_data.set_blocks_count(b.get_index())
            node_data.set_self_blocks_count(self_blocks_count)
            node_data.add_record(LogRecord(b.get_timestamp(), b.get_index(), self_blocks_count, forks_count))
            self.global_forks_count = my_globals.get_global_forks_count()

    # TODO: split save data to several methods
    def save_data(self, system, log_idx, verbose=False):
        self._create_root_dir()
        experiment_dir = self._create_experiment_dirs_files(system, verbose)
        self._create_nodes_dirs(experiment_dir, self.num_nodes)
        for i in range(self.num_nodes):
            self._create_node_files(experiment_dir, i, log_idx, verbose)

    # todo: fix load data according to changes
    def load_data(self, verbose=False):
        experiment_dir_path = os.path.join(ROOT_DIR, self.experiment_name)
        assert os.path.exists(experiment_dir_path)
        for i in range(self.num_nodes):
            node_data_file_path = os.path.join(experiment_dir_path,
                                               LOG_FILE.format(i, 0))
            singletons_file_path = os.path.join(experiment_dir_path,
                                                SINGLETONS_FILE.format(i))
            df = pd.read_pickle(node_data_file_path)
            df_singletons = pd.read_pickle(singletons_file_path)
            self.data_frames_dict[i] = df
            self.singletons_data_frames_dict[i] = df_singletons
            if verbose is True:
                print(df)
                print(df_singletons)

    def get_nodes_data(self):
        return self.nodes_data_dict

    def get_ffbi_list(self):  # ffbi = first foreign block index
        return [node_data.get_first_foreign_block_index() for node_data in self.nodes_data_dict.values()
                if node_data != -1]

    def get_sbp_lists_list(self):  # spb = self blocks percentage
        return [(i, 100 * self.nodes_data_dict[i].get_self_blocks()/self.nodes_data_dict[i].get_blocks_count())
                for i in range(self.num_nodes)]

    def get_global_forks_count(self):
        return self.global_forks_count

    @staticmethod
    def _snapshot_block_aux(b, node, forks_count, self_blocks_count,
                            node_log):
        if b.get_forks_counter() > 0:
            forks_count += b.get_forks_counter()
        if b.get_owner_id() == node.get_id():
            self_blocks_count += 1
        node_log.set_first_block_timestamp(b)
        return forks_count, self_blocks_count

    @staticmethod
    def _create_root_dir():
        if not os.path.exists(ROOT_DIR):
            os.makedirs(ROOT_DIR)

    def _create_experiment_dirs_files(self, system, verbose=False):
        experiment_dir_path = os.path.join(ROOT_DIR, self.experiment_name)
        cur_path = experiment_dir_path
        i = 1
        while os.path.exists(cur_path):
            cur_path = experiment_dir_path + "({})".format(i)
            i += 1
        experiment_dir_path = cur_path
        os.makedirs(experiment_dir_path)
        setup_file_path = os.path.join(experiment_dir_path, SETUP_FILE)
        if not os.path.exists(setup_file_path):
            with open(setup_file_path, 'w') as setup_file:
                setup_file.write(self.setup_description)
        system_pickle_file_path = os.path.join(experiment_dir_path,
                                               SYSTEM_PICKLE)
        if not os.path.exists(system_pickle_file_path):
            with open(system_pickle_file_path, 'wb') as system_pickle_file:
                pickle.dump(system, system_pickle_file)
        system_run_file_path = os.path.join(experiment_dir_path, SYSTEM_RUN_FILE)
        df = pd.DataFrame(data=[my_globals.get_global_forks_count()], columns=['Global Forks Count'])
        df.to_csv(path_or_buf=system_run_file_path)
        if verbose:
            print(self.setup_description)
            print(df)
        return experiment_dir_path

    def _create_node_files(self, dir_path, node_idx, log_idx, verbose=False):
        node_dir_path = os.path.join(dir_path, NODE_DIR.format(node_idx))
        node_log_file_path = os.path.join(node_dir_path,
                                          LOG_FILE.format(log_idx))
        singletons_file_path = os.path.join(node_dir_path,
                                            SINGLETONS_FILE.format(log_idx))
        node_data = self.nodes_data_dict[node_idx]  # type: NodeData
        df = pd.DataFrame(data=map(LogRecord.get_data_as_tuple,
                                   node_data.get_log()),
                          columns=LogRecord.columns_names())
        df_singletons = pd.DataFrame([node_data.get_singletons()],
                                     columns=NodeData.singletons_names())
        if verbose:
            print(df)
            print(df_singletons)
        df.to_csv(path_or_buf=node_log_file_path)
        df_singletons.to_csv(path_or_buf=singletons_file_path)

    def _create_nodes_dirs(self, experiment_dir_path, num_nodes):
        for i in range(num_nodes):
            node_dir_path = os.path.join(experiment_dir_path, NODE_DIR.format(i))
            if not os.path.exists(node_dir_path):
                os.makedirs(node_dir_path)
