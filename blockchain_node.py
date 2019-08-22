from blockchain_data_structures import Block
from events import BlockCreation, BlockArrival


class Node:

    def __init__(self, power, neighbors, difficulty, genesis_block,
                 node_id):
        self.power = power
        self.neighbors = neighbors
        self.difficulty = difficulty
        self.block_chain = genesis_block
        self.node_id = node_id

    def time_until_next_block(self):
        return 1

    def create_block(self, timestamp):
        new_block = Block(self.block_chain, timestamp, self.node_id)
        self.block_chain = new_block
        return new_block

    def handle_block_arrival(self, block):
        # todo: timestamp matters?
        # todo: handle epoch
        if block.block_index > self.block_chain.block_index:
            self.block_chain = block

    def generate_block_creation_event(self, global_time):
        delta = self.time_until_next_block()
        block_creation = BlockCreation(global_time + delta, self.node_id)
        return block_creation

    def send_block(self, global_time, block):
        block_arrivals = [BlockArrival(global_time + propagation_time,
                                       self.node_id, n.node_id, block)
                          for n, propagation_time in self.neighbors]
        return block_arrivals

    def print_ledger(self):
        b = self.block_chain
        while b.block_index != 0:
            print(b.block_index)
            b = b.prev_block
