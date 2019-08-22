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
            if isinstance(next_event, BlockCreation):
                creator_node = self.nodes[next_event.initiator_node_id]
                new_block = creator_node.create_block(next_event.timestamp)
                self._send_block_to_neighbors(creator_node, new_block)
                new_block_creation_event = creator_node.generate_block_creation_event(self.global_time)
                self.events_queue.put(new_block_creation_event)
                self._check_difficulty_update(creator_node)
            else:
                assert isinstance(next_event, BlockArrival)
                receiver_node = self.nodes[next_event.receiver_node_id]
                if receiver_node.handle_block_arrival(next_event.block) is True:
                    self._send_block_to_neighbors(receiver_node, next_event.block)
                    new_block_creation_event = receiver_node.generate_block_creation_event(self.global_time)
                    self.events_queue.put(new_block_creation_event)
                    self._check_difficulty_update(receiver_node)

    def _send_block_to_neighbors(self, sender_node, block):
        block_arrivals = sender_node.send_block(self.global_time, block)
        for block_arrival in block_arrivals:
            self.events_queue.put(block_arrival)

    def _create_system_nodes(self, p):
        initial_difficulty = 1. / (sum(p.power_list) * p.target_block_creation_rate)
        nodes_list = [Node(p.power_list[i], [], initial_difficulty, self.genesis_block, i)
                      for i in range(p.number_of_nodes)]
        for node in nodes_list:
            for other_node in nodes_list:
                if p.adjacency_matrix[node.node_id][other_node.node_id] > 0:
                    propagation_time = p.adjacency_matrix[node.node_id][other_node.node_id]
                    node.neighbors.append((other_node, propagation_time))
        return nodes_list

    def _check_difficulty_update(self, node):
        current_epoch = node.block_chain.block_index // self.system_static_properties.blocks_per_epoch
        if current_epoch > node.current_epoch:
            chains_block_creation_rate = node.block_chain.timestamp / node.block_chain.block_index
            update_factor = self.system_static_properties.target_block_creation_rate / chains_block_creation_rate
            new_difficulty = node.difficulty * update_factor
            node.difficulty = new_difficulty
            node.current_epoch = current_epoch

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
