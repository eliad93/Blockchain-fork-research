import queue as Q

from Block import Block
from blockchain_node import Node
from events import BlockCreation, BlockArrival


class System:

    def __init__(self, system_properties):
        self.system_properties = system_properties
        self.global_time = 0
        self.events_queue = Q.PriorityQueue()
        self.genesis_block = Block(None, 0, None)
        p = system_properties
        self.nodes = [Node(p.power_dict[i], [], p.initial_difficulty,
                           self.genesis_block, i) for i in p.number_of_nodes]
        for node in self.nodes:
            node.neighbors = []
            for other_node in self.nodes:
                if p.adjacency_matrix[node.node_id][other_node.node_id] > 0:
                    length = p.adjacency_matrix[node.node_id][other_node.node_id]
                    node.neighbors.append((other_node, length))

        self._generate_block_creations()

    def step(self):
        assert not self.events_queue.empty()

        next_event = self.events_queue.get()
        if isinstance(next_event, BlockCreation):
            block_arrivals = self.nodes[next_event.initiator_node_id]\
                .send_block(self.global_time)
            [self.events_queue.put(block_arrival)
             for block_arrival in block_arrivals]
        else:
            assert isinstance(next_event, BlockArrival)


    def _generate_block_creations(self):
        block_creations = [node.create_block(self.global_time)
                           for node in self.nodes]
        for block_creation in block_creations:
            self.events_queue.put(block_creation)


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
