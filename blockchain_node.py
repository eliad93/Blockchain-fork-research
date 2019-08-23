import numpy as np

from blockchain_data_structures import Block
from events import BlockCreation, BlockArrival


class Node:

    def __init__(self, power, neighbors, difficulty, genesis_block,
                 node_id, blocks_per_epoch, target_block_creation_rate):
        self.power = power
        self.neighbors = neighbors
        self.difficulty = difficulty
        self.block_chain = genesis_block
        self.node_id = node_id

        self.current_epoch = 0
        self.last_created_block_event = None
        self.blocks_per_epoch = blocks_per_epoch
        self.target_block_creation_rate = target_block_creation_rate

    def time_until_next_block(self):
        beta = 1. / (self.power * self.difficulty)
        return np.random.exponential(scale=beta)

    def create_block(self, timestamp):
        new_block = Block(self.block_chain, timestamp, self.node_id)
        self.block_chain = new_block
        return new_block

    def handle_block_arrival(self, block):
        # todo: timestamp matters?
        if block.block_index > self.block_chain.block_index:
            self.block_chain = block
            self.last_created_block_event.handle_event_flag = False
            return True
        return False

    def generate_block_creation_event(self, global_time):
        delta = self.time_until_next_block()
        block_creation = BlockCreation(global_time + delta, self.node_id)
        self.last_created_block_event = block_creation
        return block_creation

    def send_block(self, creation_time, block):
        block_arrivals = [BlockArrival(creation_time + propagation_time,
                                       self.node_id, n.node_id, block)
                          for n, propagation_time in self.neighbors]
        return block_arrivals

    def print_ledger(self):
        b = self.block_chain
        while b.block_index != 0:
            print(b.block_index)
            b = b.prev_block

    def check_difficulty_update(self):
        current_epoch = self.block_chain.block_index // self.blocks_per_epoch
        if current_epoch > self.current_epoch:
            chains_block_creation_rate = self.block_chain.timestamp / self.block_chain.block_index
            update_factor = self.target_block_creation_rate / chains_block_creation_rate
            new_difficulty = self.difficulty * update_factor
            self.difficulty = new_difficulty
            self.current_epoch = current_epoch
