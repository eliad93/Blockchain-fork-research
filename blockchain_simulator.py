import queue as Q

from blockchain_data_structures import Block
from blockchain_node import Node
from events import BlockCreation, BlockArrival


class System:

    def __init__(self, system_static_properties):
        self.static_properties = system_static_properties
        self.global_time = 0.
        self.events_queue = Q.PriorityQueue()
        self.genesis_block = Block(None, 0., None, None)
        self.nodes = self._create_system_nodes()
        self._generate_block_creation_events()

    def step(self):
        assert not self.events_queue.empty()

        next_event = self.events_queue.get()
        self.global_time = next_event.get_timestamp()

        if next_event.get_handle_event_flag() is True:
            if isinstance(next_event, BlockCreation):
                creator_node = self.nodes[next_event.get_initiator_node_id()]
                new_block_creation_event, block_arrival_events = creator_node.handle_block_creation_event(next_event)
                for event in [new_block_creation_event] + block_arrival_events:
                    self.events_queue.put(event)
            else:
                assert isinstance(next_event, BlockArrival)
                receiver_node = self.nodes[next_event.get_receiver_node_id()]
                new_block_creation_event, block_arrival_events = receiver_node.handle_block_arrival(next_event)
                if new_block_creation_event is not None:
                    for event in [new_block_creation_event] + block_arrival_events:
                        self.events_queue.put(event)

    def print_nodes_ledgers(self):
        for node in self.nodes:
            node.print_ledger()

    def _create_system_nodes(self):
        p = self.static_properties
        initial_difficulty = 1. / (p.get_powers_sum() * p.get_target_block_creation_rate())
        nodes_list = [Node(p.get_power_by_node_id(i), [], initial_difficulty, self.genesis_block, i,
                           p.get_blocks_per_epoch(), p.get_target_block_creation_rate())
                      for i in range(p.get_number_of_nodes())]
        for node in nodes_list:
            for other_node in nodes_list:
                propagation_time = p.get_adjacency_matrix_cell(node.get_id(), other_node.get_id())
                if propagation_time > 0:
                    node.add_neighbor(other_node, propagation_time)
        return nodes_list

    def _generate_block_creation_events(self):
        block_creation_events = [node.generate_block_creation_event(self.global_time) for node in self.nodes]
        for event in block_creation_events:
            self.events_queue.put(event)


class SystemProperties:

    def __init__(self, adjacency_matrix, power_list, blocks_per_epoch, target_block_creation_rate):
        self.adjacency_matrix = adjacency_matrix
        self.number_of_nodes = len(adjacency_matrix)
        self.power_list = power_list
        self.blocks_per_epoch = blocks_per_epoch
        self.target_block_creation_rate = target_block_creation_rate

    def get_adjacency_matrix_cell(self, i, j):
        return self.adjacency_matrix[i][j]

    def get_number_of_nodes(self):
        return self.number_of_nodes

    def get_power_by_node_id(self, node_index):
        return self.power_list[node_index]

    def get_powers_sum(self):
        return sum(self.power_list)

    def get_blocks_per_epoch(self):
        return self.blocks_per_epoch

    def get_target_block_creation_rate(self):
        return self.target_block_creation_rate
