import numpy as np

from blockchain_data_structures import Block
from events import BlockCreation, BlockArrival


class Node:

    def __init__(self, power, neighbors, genesis_block, node_id):
        self.power = power  # mining power
        self.neighbors = neighbors  # other nodes that are connected directly
        self.block_chain = genesis_block
        self.node_id = node_id  # unique in the system
        self.last_created_block_event = None

    def get_id(self):
        return self.node_id

    def get_block_chain(self):
        return self.block_chain

    def add_neighbor(self, node, propagation_time):
        self.neighbors.append((node, propagation_time))

    def handle_block_creation_event(self, block_creation_event):
        timestamp = block_creation_event.get_timestamp()
        new_block = self._create_block(timestamp)
        block_arrival_events = \
            self._send_block_to_neighbors(new_block, timestamp)
        new_block_creation_event = self.generate_block_creation_event(timestamp)
        return new_block_creation_event, block_arrival_events

    def handle_block_arrival(self, block_arrival_event):
        block = block_arrival_event.get_block()
        timestamp = block_arrival_event.get_timestamp()
        if block.get_index() > self.block_chain.get_index():
            self.block_chain = block
            self.last_created_block_event.set_handle_event_flag(False)
            block_arrival_events = \
                self._send_block_to_neighbors(block, timestamp)
            new_block_creation_event = \
                self.generate_block_creation_event(timestamp)
            return new_block_creation_event, block_arrival_events
        return None, None

    def generate_block_creation_event(self, global_time):
        delta = self._time_until_next_block()
        block_creation_event = BlockCreation(global_time + delta, self.node_id)
        self.last_created_block_event = block_creation_event
        return block_creation_event

    def print_ledger(self):
        b = self.block_chain
        print("node_id: {}". format(self.node_id))
        while b.get_index() != 0:
            print("block_index: {} block_time {} owner_id: {}"
                  .format(b.get_index(), b.get_timestamp(), b.get_owner_id()))
            b = b.get_prev()

    def print_forks_ledger(self):
        number_of_forks = 0
        b = self.block_chain
        print("Node's id: {}".format(self.node_id))
        while b.get_index() > 0:
            if b.get_forks_counter() > 0:
                number_of_forks += b.get_forks_counter()
                print("There was fork in block: {}.\nblock creation time {}, block's owner: {}, number of forks: {}"
                    .format(b.get_index(), b.get_timestamp(), b.get_owner_id(), b.get_forks_counter()))
            b = b.get_prev()
        if b.get_forks_counter() > 0:
            number_of_forks += b.get_forks_counter()
            print("Number of forks in genesis block: {}\nTotal number of forks in the node's chain is: {}\nForks per blocks: {}".format(
                b.get_forks_counter(), number_of_forks, self.block_chain.get_index() / number_of_forks))

    def _create_block(self, timestamp):
        new_block = Block(self.block_chain, timestamp, self.node_id, None,
                          None, None)
        self.block_chain = new_block
        return new_block

    def _time_until_next_block(self):
        beta = 1. / (self.power * self.block_chain.get_difficulty())
        return np.random.exponential(scale=beta)

    def _send_block_to_neighbors(self, block, timestamp):
        block_arrival_events = \
            [BlockArrival(timestamp + propagation_time, self.node_id,
                          neighbor.get_id(), block)
             for neighbor, propagation_time in self.neighbors]
        return block_arrival_events

    def print_accepted_blocks(self):
        b = self.block_chain
        print("node_id: {}".format(self.node_id))
        total_accepted = 0
        while b.get_index() != 0:
            if b.get_index() != self.node_id:
                total_accepted += 1
                print("block_index: {} block_time {} owner_id: {}".format(
                    b.get_index(), b.get_timestamp(),
                    b.get_owner_id()))
            b = b.get_prev()
        print("\n\n\nTotal number of accepted blocks is {}".format(total_accepted))
