# Class for a block in a blockchain.
# Params:
#               prev_block: Previous block in the chain. If the block is the first one in the chain then None.
#               timestamp: Creation time.
#               owner_id: ID of creator/miner.
#               difficulty: The current difficulty of the chain. Difficulty to mine/create new block.
#               blocks_per_epoch: The number of blocks in an epoch. Every time a new epoch starts the difficulty is
#               updated.
#               target_time_between_blocks: A parameter needed for difficulty update.
# Other fields:
#               block_index: The index of the block in the blockchain. The genesis block's index is 0.
#               epoch_first_block: The first block in the block's epoch in the chain.
#               forks_counter: The number of forks from the block. If the block is the previous block of more than
#                              1 block than the counter increases.
class Block:

    def __init__(self, prev_block, timestamp, owner_id, difficulty,
                 blocks_per_epoch, target_time_between_blocks):
        self.prev_block = prev_block
        self.timestamp = timestamp  # block creation time
        self.owner_id = owner_id  # the id of the creating node
        self.block_index = 0 if prev_block is None \
            else prev_block.block_index + 1  # a running counter
        self.difficulty = difficulty if prev_block is None else \
            prev_block.difficulty  # the mining difficulty this block created
        self.blocks_per_epoch = blocks_per_epoch if prev_block is None \
            else prev_block.blocks_per_epoch
        self.target_time_between_blocks = target_time_between_blocks \
            if prev_block is None else prev_block.target_time_between_blocks
        if prev_block is None:
            self.epoch_first_block = None
        else:
            index_in_epoch = self.block_index % self.blocks_per_epoch
            self.epoch_first_block = self if index_in_epoch == 1 \
                else prev_block.epoch_first_block
        self._check_difficulty_update()
        self.forks_counter = -1
        if prev_block is not None:
            prev_block.forks_counter += 1

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

    def get_forks_counter(self):
        return self.forks_counter

    # Here the difficulty update is executed (logic is similar to bitcoin).
    def _check_difficulty_update(self):
        if self == self.epoch_first_block and self.block_index > 1:
            quanta = self.prev_block.timestamp - \
                     self.prev_block.epoch_first_block.timestamp
            epoch_time_between_blocks = quanta / self.blocks_per_epoch
            update_factor = \
                epoch_time_between_blocks / self.target_time_between_blocks
            new_difficulty = self.difficulty * update_factor
            self.difficulty = new_difficulty
