import queue
from heapq import heappush, heappop

from blockchain_data_structures import Block
from blockchain_node import Node
from events import BlockCreation, BlockArrival

# Main class that contains all system's data
# Params:
#               graph_name: The name of the graph.
#               static_properties: Contain all initial static properties of the system (SystemProperties class).
#               global_time: The system's current time.
# Other fields:
#               events_queue: Queue with all upcoming events in the system (BlockCreation, BlockArrival).
#               genesis_block: First block in the system.
#               nodes: All system's nodes/users.
class System:
    
    def __init__(self, graph_name, static_properties):
        self.graph_name = graph_name
        self.static_properties = static_properties
        self.global_time = 0.
        self.events_queue = []
        initial_difficulty = 1. / float(
            static_properties.get_powers_sum() *
            static_properties.get_target_block_creation_rate())
        self.genesis_block = Block(None, self.global_time, None,
                                   initial_difficulty,
                                   static_properties.get_blocks_per_epoch(),
                                   static_properties.get_target_block_creation_rate())
        self.nodes = self._create_system_nodes()
        self._generate_block_creation_events()

    def step(self):
        assert not len(self.events_queue) == 0

        next_event = heappop(self.events_queue)
        self.global_time = next_event.get_timestamp()

        if next_event.get_handle_event_flag() is True:
            if isinstance(next_event, BlockCreation):
                creator_node = self.nodes[next_event.get_initiator_node_id()]
                new_block_creation_event, block_arrival_events = \
                    creator_node.handle_block_creation_event(next_event)
                for event in [new_block_creation_event] + block_arrival_events:
                    heappush(self.events_queue, event)

            else:
                assert isinstance(next_event, BlockArrival)
                receiver_node = self.nodes[next_event.get_receiver_node_id()]
                new_block_creation_event, block_arrival_events = \
                    receiver_node.handle_block_arrival(next_event)
                # new_block_creation_event is None if the arrived block was not accepted
                if new_block_creation_event is not None:
                    for event in [new_block_creation_event] + \
                                 block_arrival_events:
                        heappush(self.events_queue, event)
        return next_event

    def print_nodes_ledgers(self):
        print("graph_name {}:".format(self.graph_name))
        for node in self.nodes:
            # node.print_ledger()
            node.print_forks_ledger()
            print("=======================================")

    def _create_system_nodes(self):
        p = self.static_properties
        nodes_list = [Node(p.get_power_by_node_id(i), [], self.genesis_block, i)
                      for i in range(p.get_number_of_nodes())]
        for node in nodes_list:
            for other_node in nodes_list:
                if node.get_id() != other_node.get_id():
                    propagation_time = p.get_adjacency_matrix_cell(
                        node.get_id(), other_node.get_id())
                    if propagation_time >= 0:
                        node.add_neighbor(other_node, propagation_time)
        return nodes_list

    def _generate_block_creation_events(self):
        block_creation_events = [
            node.generate_block_creation_event(self.global_time) for node in
            self.nodes]
        for event in block_creation_events:
            heappush(self.events_queue, event)

    def print_nodes_accepted_blocks(self):
        print("graph_name {}:".format(self.graph_name))
        for node in self.nodes:
            node.print_accepted_blocks()
            print("=======================================")

    def get_num_nodes(self):
        return len(self.nodes)

    def get_nodes(self):
        return self.nodes

    def get_static_properties(self):
        return self.static_properties

    def setup_description(self):
        sp = self.get_static_properties()
        setup_description = "# graph name: {}\n# number of nodes: {}\n" \
                            "# power list\n{}\n# blocks per epoch: {}\n" \
                            "# target block creation rate: {}"\
            .format(self.graph_name, self.get_num_nodes(),
                    sp.get_power_list(), sp.get_blocks_per_epoch(),
                    sp.get_target_block_creation_rate())
        return setup_description

# Class for system's static properties
# Params:
#           adjacency_matrix: The topology of the graph. adjacency_matrix[i][j] == "distance" (actually latency)
#           from node i to j.
#           power_list: List with the system's nodes powers. power_list[i] == power of node i.
#           blocks_per_epoch: Number of blocks per epoch.
#           target_block_creation_rate: Wanted blocks creation rate.
class SystemProperties:

    def __init__(self, adjacency_matrix, power_list, blocks_per_epoch,
                 target_block_creation_rate):
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

    def get_power_list(self):
        return self.power_list
