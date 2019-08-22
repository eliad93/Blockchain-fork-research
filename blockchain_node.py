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

    def create_block(self, global_time):
        delta = self.time_until_next_block()
        block_creation = BlockCreation(global_time + delta, self.node_id)
        return block_creation

    def send_block(self, global_time):
        block_arrivals = [BlockArrival(global_time + length,
                                       self.node_id, n.node_id)
                          for n, length in self.neighbors]
        return block_arrivals
