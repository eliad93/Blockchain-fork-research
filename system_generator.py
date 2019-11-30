# TODO: number of steps, size of step, which parametr to change
from collections import Iterable

from system import SystemProperties, System


class SystemGenerator:
    def __init__(self, adjacency_matrix, power_lists: list,
                 blocks_per_epoch_list: list,
                 target_block_creation_rates: list,
                 graph_name):
        self.power_lists = power_lists
        self.blocks_per_epoch_list = blocks_per_epoch_list
        self.target_block_creation_rates = target_block_creation_rates
        self.adjacency_matrix = adjacency_matrix
        self.graph_name = graph_name
        self.system = None

    def generate(self):
        for power_list in self.power_lists:
            for blocks_per_epoch in self.blocks_per_epoch_list:
                for target_block_creation_rate \
                        in self.target_block_creation_rates:
                    system_props = SystemProperties(self.adjacency_matrix,
                                                    power_list,
                                                    blocks_per_epoch,
                                                    target_block_creation_rate)
                    self.system = System(self.graph_name, system_props)
                    yield self.system
