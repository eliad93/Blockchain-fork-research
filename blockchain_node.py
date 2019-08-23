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

    def _create_block(self, timestamp):
        epoch_first_block = None if self._is_last_epoch_block() \
            else self.block_chain.epoch_first_block
        new_block = Block(self.block_chain, timestamp,
                          self.node_id, epoch_first_block)
        self.block_chain = new_block
        return new_block

    def handle_block_creation_event(self, block_creation_event):
        timestamp = block_creation_event.timestamp
        new_block = self._create_block(timestamp)
        block_arrivals = self._send_block_to_neighbors(new_block, timestamp)
        new_block_creation_event = self.generate_block_creation_event(timestamp)
        self._check_difficulty_update()
        return new_block_creation_event, block_arrivals

    def handle_block_arrival(self, block_arrival_event):
        # todo: timestamp matters?
        block = block_arrival_event.block
        timestamp = block_arrival_event.timestamp
        if block.block_index > self.block_chain.block_index:
            self.block_chain = block
            self.last_created_block_event.handle_event_flag = False
            block_arrivals = self._send_block_to_neighbors(block, timestamp)
            self._check_difficulty_update()
            new_block_creation_event = \
                self.generate_block_creation_event(timestamp)
            return new_block_creation_event, block_arrivals
        return None, None

    def generate_block_creation_event(self, global_time):
        delta = self._time_until_next_block()
        block_creation = BlockCreation(global_time + delta, self.node_id)
        self.last_created_block_event = block_creation
        return block_creation

    def print_ledger(self):
        b = self.block_chain
        while b.block_index != 0:
            print(b.block_index)
            b = b.prev_block

    def _time_until_next_block(self):
        beta = 1. / (self.power * self.difficulty)
        return np.random.exponential(scale=beta)

    def _send_block_to_neighbors(self, block, timestamp):
        block_arrivals = [BlockArrival(timestamp + propagation_time,
                                       self.node_id, n.node_id, block)
                          for n, propagation_time in self.neighbors]
        return block_arrivals

    def _check_difficulty_update(self):
        current_epoch = self.block_chain.block_index // self.blocks_per_epoch
        if current_epoch > self.current_epoch:
            # todo: consider only last epoch
            last_complete_epoch_block = self._last_complete_epoch_block()
            quanta = last_complete_epoch_block.timestamp - \
                last_complete_epoch_block.epoch_first_block.timestamp
            chains_block_creation_rate = quanta / self.blocks_per_epoch
            update_factor = \
                self.target_block_creation_rate / chains_block_creation_rate
            new_difficulty = self.difficulty * update_factor
            self.difficulty = new_difficulty
            self.current_epoch = current_epoch

    def _last_complete_epoch_block(self):
        return self.block_chain if self._is_last_epoch_block() \
            else self.block_chain.epoch_first_block.prev

    def _is_last_epoch_block(self):
        return ((self.block_chain.block_index + 1) % self.blocks_per_epoch) == \
               0 and (self.block_chain.block_index // self.blocks_per_epoch) == \
               self.current_epoch
