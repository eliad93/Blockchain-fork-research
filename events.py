import abc


class SystemEvent(abc.ABC):

    def __init__(self, timestamp, node_id):
        self.timestamp = timestamp
        self.initiator_node_id = node_id

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class BlockCreation(SystemEvent):

    def __init__(self, timestamp, node_id):
        super().__init__(timestamp, node_id)


class BlockArrival(SystemEvent):

    def __init__(self, timestamp, node_id, receiver_node_id):
        super().__init__(timestamp, node_id)
        self.receiver_node_id = receiver_node_id
