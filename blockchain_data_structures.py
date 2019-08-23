
class Block:

    def __init__(self, prev_block, timestamp, owner_id, epoch_first_block):
        self.block_index = prev_block.block_index + 1 \
            if prev_block is not None else 0
        self.prev_block = prev_block
        self.timestamp = timestamp
        self.owner_id = owner_id
        self.epoch_first_block = epoch_first_block \
            if epoch_first_block is not None else self

    def is_epoch_first_block(self):
        return self == self.epoch_first_block

