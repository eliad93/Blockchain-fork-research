import copy
from typing import Iterable

import numpy as np

from events import BlockArrival
from simulator_log import SimulatorLog
from system import System

# TODO: Add multiple runs and averages to all necessary output
from system_generator import SystemGenerator


# Helper class for running simulations.
class Simulator:
    def __init__(self, systems: SystemGenerator):
        self.systems = systems
        self.initial_system = None  # enables multiple runs
        self.system = None  # current active system
        self.log = None

    def hyper_run(self, experiment_name=None, iterations=100,
                  block_arrivals_per_snapshot=1, reps=1, verbose=False):
        for sys in self.systems.generate():
            self.initial_system = copy.deepcopy(sys)
            self.run_simulation(experiment_name, iterations,
                                block_arrivals_per_snapshot, reps, verbose)

    def run_simulation(self, experiment_name=None, iterations=100,
                       block_arrivals_per_snapshot=1, reps=1, verbose=False,
                       system=None):
        if system:
            self.initial_system = copy.deepcopy(system)
        logs = []
        for rep in range(reps):
            self._reset_system()
            logs.append(self._run(experiment_name, iterations,
                                  block_arrivals_per_snapshot))
        ffbi_list = self._extract_ffbi_from_logs(logs)
        ffbi_avg = np.mean(ffbi_list)
        if verbose:
            print(ffbi_avg)
        self._save_data(logs, verbose=verbose)

    def _run(self, experiment_name=None, iterations=100,
             block_arrivals_per_snapshot=1):
        log = SimulatorLog(self.system.get_num_nodes(), experiment_name,
                           self.system.setup_description())
        num_block_arrivals = 0
        for i in range(iterations):
            current_event = self.system.step()
            if isinstance(current_event, BlockArrival):
                num_block_arrivals += 1
                if num_block_arrivals % block_arrivals_per_snapshot == 0:
                    log.snapshot_blockchains(self.system.get_nodes())
        return log

    def _reset_system(self):
        self.system = copy.deepcopy(self.initial_system)

    @staticmethod
    def _extract_ffbi_from_logs(logs):
        ffbi_list = [[min(log.get_ffbi_list())] for log in logs]
        return ffbi_list

    def _save_data(self, logs, verbose):
        for i, log in enumerate(logs):
            log.save_data(self.initial_system, i, verbose=verbose)
