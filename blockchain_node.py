import numpy as np

from blockchain_data_structures import Block
from events import BlockCreation, BlockArrival


class Node:

    def __init__(self, power, neighbors, difficulty, genesis_block,
                 node_id, blocks_per_epoch, target_time_between_blocks):
        self.power = power
        self.neighbors = neighbors
        self.difficulty = difficulty
        self.block_chain = genesis_block
        self.node_id = node_id
        self.current_epoch = 0
        self.last_created_block_event = None
        self.blocks_per_epoch = blocks_per_epoch
        self.target_time_between_blocks = target_time_between_blocks

    def get_id(self):
        return self.node_id

    def add_neighbor(self, node, propagation_time):
        self.neighbors.append((node, propagation_time))

    def handle_block_creation_event(self, block_creation_event):
        timestamp = block_creation_event.get_timestamp()
        new_block = self._create_block(timestamp)
        block_arrival_events = self._send_block_to_neighbors(new_block, timestamp)
        new_block_creation_event = self.generate_block_creation_event(timestamp)
        self._check_difficulty_update()
        return new_block_creation_event, block_arrival_events

    def handle_block_arrival(self, block_arrival_event):
        # todo: Take chain with lower timestamp when two chains have the same length?
        block = block_arrival_event.get_block()
        timestamp = block_arrival_event.get_timestamp()
        if block.get_index() > self.block_chain.get_index():
            self.block_chain = block
            self.last_created_block_event.set_handle_event_flag(False)
            block_arrival_events = self._send_block_to_neighbors(block, timestamp)
            self._check_difficulty_update()
            new_block_creation_event = self.generate_block_creation_event(timestamp)
            return new_block_creation_event, block_arrival_events
        return None, None

    def generate_block_creation_event(self, global_time):
        delta = self._time_until_next_block()
        block_creation_event = BlockCreation(global_time + delta, self.node_id)
        self.last_created_block_event = block_creation_event
        return block_creation_event

    def print_ledger(self):
        b = self.block_chain
        while b.get_index() != 0:
            print("block_index: {} block_time {} owner_id: {}".format(b.get_index(), b.get_timestamp(),
                                                                      b.get_owner_id()))
            b = b.get_prev()

    def _create_block(self, timestamp):
        epoch_first_block = None if self._is_last_block_in_epoch() else self.block_chain.get_epoch_first_block()
        new_block = Block(self.block_chain, timestamp, self.node_id, epoch_first_block)
        self.block_chain = new_block
        return new_block

    def _time_until_next_block(self):
        beta = 1. / (self.power * self.difficulty)
        return np.random.exponential(scale=beta)

    def _send_block_to_neighbors(self, block, timestamp):
        block_arrival_events = [BlockArrival(timestamp + propagation_time, self.node_id, n.get_id(), block)
                                for n, propagation_time in self.neighbors]
        return block_arrival_events

    def _check_difficulty_update(self):
        current_epoch = self.block_chain.get_index() // self.blocks_per_epoch
        if current_epoch > self.current_epoch:
            last_block = self.block_chain.get_last_block_in_last_complete_epoch()
            quanta = last_block.get_timestamp() - last_block.get_epoch_beginning_timestamp()
            epoch_time_between_blocks = quanta / self.blocks_per_epoch
            update_factor = epoch_time_between_blocks / self.target_time_between_blocks
            new_difficulty = self.difficulty * update_factor
            self.difficulty = new_difficulty
            self.current_epoch = current_epoch

    def _is_last_block_in_epoch(self):
        return ((self.block_chain.get_index() + 1) % self.blocks_per_epoch) == 0 and \
               (self.block_chain.get_index() // self.blocks_per_epoch) == self.current_epoch
