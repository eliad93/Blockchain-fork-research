import copy

from events import BlockArrival
from simulator_log import SimulatorLog
from system import System

#TODO: Add multiple runs and averages to all necessary output
class Simulator:
    """
    Helper class for running simulations.
    """

    def __init__(self, system: System):
        self.initial_system = copy.deepcopy(system)  # enables multiple runs
        self.system = copy.deepcopy(system)  # current active system
        self.log = None

    def run(self, experiment_name=None, iterations=100,
            block_arrivals_per_snapshot=1):
        self.log = SimulatorLog(self.system.get_num_nodes(), experiment_name,
                                self.system.setup_description())
        num_block_arrivals = 0
        for i in range(iterations):
            current_event = self.system.step()
            if isinstance(current_event, BlockArrival):
                num_block_arrivals += 1
                if num_block_arrivals % block_arrivals_per_snapshot == 0:
                    self.log.snapshot_blockchains(self.system.get_nodes())
        self.log.save_data(verbose=True)
        self.log.load_data(verbose=False)
