class Block:

    def __init__(self, prev_block, timestamp, owner_id, difficulty, blocks_per_epoch,
                 target_time_between_blocks):
        self.prev_block = prev_block
        self.timestamp = timestamp
        self.owner_id = owner_id
        self.block_index = 0 if prev_block is None else prev_block.block_index + 1
        self.difficulty = difficulty if prev_block is None else prev_block.difficulty
        self.blocks_per_epoch = blocks_per_epoch if prev_block is None else prev_block.blocks_per_epoch
        self.target_time_between_blocks = target_time_between_blocks if prev_block is None else \
            prev_block.target_time_between_blocks
        if prev_block is None:
            self.epoch_first_block = None
        else:
            index_in_epoch = self.block_index % self.blocks_per_epoch
            self.epoch_first_block = self if index_in_epoch == 1 else prev_block.epoch_first_block
        self._check_difficulty_update()

    def get_index(self):
        return self.block_index

    def get_owner_id(self):
        return self.owner_id

    def get_prev(self):
        return self.prev_block

    def get_timestamp(self):
        return self.timestamp

    def get_difficulty(self):
        return self.difficulty

    def _check_difficulty_update(self):
        if self == self.epoch_first_block and self.block_index > 1:
            quanta = self.prev_block.timestamp - self.prev_block.epoch_first_block.timestamp
            epoch_time_between_blocks = quanta / self.blocks_per_epoch
            update_factor = epoch_time_between_blocks / self.target_time_between_blocks
            new_difficulty = self.difficulty * update_factor
            self.difficulty = new_difficulty
