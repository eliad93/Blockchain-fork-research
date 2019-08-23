import queue as Q

from blockchain_data_structures import Block
from blockchain_node import Node
from events import BlockCreation, BlockArrival


class System:

    def __init__(self, system_static_properties):
        self.system_static_properties = system_static_properties
        self.global_time = 0.
        self.events_queue = Q.PriorityQueue()
        self.genesis_block = Block(None, 0., None)
        self.nodes = self._create_system_nodes(system_static_properties)
        self._generate_block_creation_events()

    def step(self):
        assert not self.events_queue.empty()

        next_event = self.events_queue.get()
        self.global_time = next_event.timestamp

        if next_event.handle_event_flag is True:
            # todo: insert logic into node
            if isinstance(next_event, BlockCreation):
                creator_node = self.nodes[next_event.initiator_node_id]
                new_block_creation_event, block_arrivals = \
                    creator_node.create_block(next_event.timestamp)
                for block_arrival in block_arrivals:
                    self.events_queue.put(block_arrival)
                self.events_queue.put(new_block_creation_event)
            else:
                assert isinstance(next_event, BlockArrival)
                receiver_node = self.nodes[next_event.receiver_node_id]
                new_block_creation_event, block_arrivals = \
                    receiver_node.handle_block_arrival(next_event)
                if new_block_creation_event is not None:
                    for block_arrival in block_arrivals:
                        self.events_queue.put(block_arrival)
                    self.events_queue.put(new_block_creation_event)

    def _send_block_to_neighbors(self, sender_node, block):
        block_arrivals = sender_node.send_block(self.global_time, block)
        for block_arrival in block_arrivals:
            self.events_queue.put(block_arrival)

    def _create_system_nodes(self, p):
        initial_difficulty = 1. / (sum(p.power_list) * p.target_block_creation_rate)
        nodes_list = [Node(p.power_list[i], [], initial_difficulty, self.genesis_block, i,
                           self.system_static_properties.blocks_per_epoch,
                           self.system_static_properties.target_block_creation_rate)
                      for i in range(p.number_of_nodes)]
        for node in nodes_list:
            for other_node in nodes_list:
                if p.adjacency_matrix[node.node_id][other_node.node_id] > 0:
                    propagation_time = p.adjacency_matrix[node.node_id][other_node.node_id]
                    node.neighbors.append((other_node, propagation_time))
        return nodes_list

    def _generate_block_creation_events(self):
        block_creations = [node.generate_block_creation_event(self.global_time)
                           for node in self.nodes]
        for block_creation in block_creations:
            self.events_queue.put(block_creation)

    def print_nodes_ledgers(self):
        for node in self.nodes:
            node.print_ledger()


class SystemProperties:

    def __init__(self, adjacency_matrix, power_list,
                 blocks_per_epoch, target_block_creation_rate):
        self.adjacency_matrix = adjacency_matrix
        self.number_of_nodes = len(adjacency_matrix)
        self.power_list = power_list
        self.blocks_per_epoch = blocks_per_epoch
        self.target_block_creation_rate = target_block_creation_rate
