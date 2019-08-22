
class Block:

    def __init__(self, prev_block, timestamp, owner_id):
        self.block_index = prev_block.block_index + 1 if prev_block is not None else 0
        self.prev_block = prev_block
        self.timestamp = timestamp
        self.owner_id = owner_id

