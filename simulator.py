import copy
import os

import numpy as np
import pandas

from simulator_log import SimulatorLog
import my_globals


# TODO: Add multiple runs and averages to all necessary output


# Helper class for running simulations.
from system import System


class Simulator:
    def __init__(self):
        self.initial_system = None  # enables multiple runs
        self.system = None  # current active system
        self.log = None

    def hyper_run(self, systems, experiment_name=None, iterations=100,
                  block_arrivals_per_snapshot=1, reps=1, verbose=False):
        for sys in systems.generate():
            self.initial_system = copy.deepcopy(sys)
            self.run_system(experiment_name, iterations,
                            block_arrivals_per_snapshot, reps, verbose)

    def run_system(self, experiment_name=None, iterations=100,
                   block_arrivals_per_snapshot=1, reps=1, verbose=False,
                   system=None):
        if system:
            self.initial_system = copy.deepcopy(system)
        logs = []
        for rep in range(reps):
            self._reset_system()
            logs.append(self._run(experiment_name, iterations,
                                  block_arrivals_per_snapshot))
        return logs
        # ffbi_list, sbp_list, global_forks_count_list, meeting_percentage, node_ffbi_lists_list = self._extract_data_from_logs(logs)
        # ffbi_avg = np.mean(ffbi_list)
        # sbp_avg_by_node_list = [np.mean(sbp) for sbp in sbp_list]
        # global_forks_avg = np.mean(global_forks_count_list)
        # return ffbi_avg, sbp_avg_by_node_list, global_forks_avg, meeting_percentage, node_ffbi_lists_list

    def _run(self, experiment_name=None, iterations=100,
             block_arrivals_per_snapshot=1):
        my_globals.reset_globals()
        log = SimulatorLog(self.system, experiment_name,
                           self.system.setup_description())
        # num_block_arrivals = 0
        for i in range(iterations):
            current_event = self.system.step()
            # if isinstance(current_event, BlockArrival):
            #     num_block_arrivals += 1
                # if num_block_arrivals % block_arrivals_per_snapshot == 0:
                #     log.snapshot_blockchains(self.system.get_nodes())
        log.snapshot_blockchains(self.system.get_nodes())
        return log

    def _reset_system(self):
        self.system = copy.deepcopy(self.initial_system)

    @staticmethod
    def _extract_data_from_logs(logs):
        ffbi_list = []
        node_ffbi_lists_list = [log.get_ffbi_node_idx_tuple_list() for log in logs]
        for log in logs:
            min_ffbi = min(log.get_ffbi_list(), default=-1)
            if min_ffbi > -1:
                ffbi_list.append(min_ffbi)
        meeting_percentage = 100 * float(len(ffbi_list)) / float(len(logs))
        sbp_lists_list = [log.get_sbp_lists_list() for log in logs]
        sbp_by_node = [[] for i in range(len(sbp_lists_list[0]))]
        for sbp_list in sbp_lists_list:
            for i in range(len(sbp_list)):
                sbp_by_node[i].append(sbp_list[i][1])
        global_forks_count_list = [log.get_global_forks_count() for log in logs]
        return ffbi_list, sbp_by_node, global_forks_count_list, meeting_percentage, node_ffbi_lists_list

    def _save_data(self, logs, verbose):
        for i, log in enumerate(logs):
            log.save_data(self.initial_system, i, verbose=verbose)

    def _system_run_to_csv(self, experiment_name, iterations, reps, ffbi_avg, sbp_avg_by_node_list, global_forks_avg):
        columns = ["First Foreign Block Index Average", "Node Number", "Self Block Percentage Average",
                   "Global Forks Average"]
        data = [ffbi_avg, range(sbp_avg_by_node_list), sbp_avg_by_node_list, global_forks_avg]
        df = pandas.DataFrame(data=data, columns=columns)
        dir_path = os.path.join(os.getcwd(), "graphs_data")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = os.path.join(dir_path, experiment_name)
        df.to_csv(path_or_buf=file_path)
        columns = ["First Foreign Block Index Average", "Global Forks Average"]
