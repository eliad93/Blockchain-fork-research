import queue as Q

from blockchain_data_structures import Block
from blockchain_node import Node
from events import BlockCreation, BlockArrival


class System:

    def __init__(self, system_properties):
        self.system_properties = system_properties
        self.global_time = 0
        self.events_queue = Q.PriorityQueue()
        self.genesis_block = Block(None, 0, None)
        p = system_properties
        self.nodes = [Node(p.power_dict[i], [],
                           p.initial_difficulty, self.genesis_block, i)
                      for i in range(p.number_of_nodes)]
        for node in self.nodes:
            node.neighbors = []
            for other_node in self.nodes:
                if p.adjacency_matrix[node.node_id][other_node.node_id] > 0:
                    propagation_time = \
                        p.adjacency_matrix[node.node_id][other_node.node_id]
                    node.neighbors.append((other_node, propagation_time))

        self._generate_block_creation_events()

    def step(self):
        assert not self.events_queue.empty()

        next_event = self.events_queue.get()
        if isinstance(next_event, BlockCreation):
            # todo: add another block creation event
            creator_node = self.nodes[next_event.initiator_node_id]
            new_block = creator_node.create_block(next_event.timestamp)
            self._send_block_to_neighbors(creator_node, new_block)
        else:
            assert isinstance(next_event, BlockArrival)
            receiver_node = self.nodes[next_event.receiver_node_id]
            receiver_node.handle_block_arrival(next_event.block)
            self._send_block_to_neighbors(receiver_node, next_event.block)

    def _send_block_to_neighbors(self, sender_node, block):
        block_arrivals = sender_node.send_block(self.global_time, block)
        for block_arrival in block_arrivals:
            self.events_queue.put(block_arrival)

    def _generate_block_creation_events(self):
        block_creations = [node.generate_block_creation_event(self.global_time)
                           for node in self.nodes]
        for block_creation in block_creations:
            self.events_queue.put(block_creation)

    def print_nodes_ledgers(self):
        for node in self.nodes:
            node.print_ledger()


class SystemProperties:

    def __init__(self, adjacency_matrix, power_dict,
                 blocks_per_epoch, initial_difficulty,
                 target_block_creation_rate):
        self.adjacency_matrix = adjacency_matrix
        self.number_of_nodes = len(adjacency_matrix)
        self.power_dict = power_dict
        self.blocks_per_epoch = blocks_per_epoch
        self.initial_difficulty = initial_difficulty
        self.target_block_creation_rate = target_block_creation_rate
