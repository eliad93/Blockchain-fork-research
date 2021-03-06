import abc


# Abstract class for block events
# Params:
#           timestamp: Creation time.
#           initiator_node_id: ID of event's creator node.
#           handle_event_flag: If flag is False, the event will be ignored.
class SystemEvent(abc.ABC):

    def __init__(self, timestamp, node_id):
        self.timestamp = timestamp
        self.initiator_node_id = node_id
        self.handle_event_flag = True

    def __lt__(self, other):
        return self.timestamp < other.timestamp

    def get_timestamp(self):
        return self.timestamp

    def get_initiator_node_id(self):
        return self.initiator_node_id

    def get_handle_event_flag(self):
        return self.handle_event_flag

    def set_handle_event_flag(self, value):
        self.handle_event_flag = value


# Class of block creation event
class BlockCreation(SystemEvent):

    def __init__(self, timestamp, node_id):
        super().__init__(timestamp, node_id)


# Class of block arrival event
# Params:
#           receiver_node_id: ID of the receiver node.
#           block: The arrived block.
class BlockArrival(SystemEvent):

    def __init__(self, timestamp, node_id, receiver_node_id, block):
        super().__init__(timestamp, node_id)
        self.receiver_node_id = receiver_node_id
        self.block = block

    def get_receiver_node_id(self):
        return self.receiver_node_id

    def get_block(self):
        return self.block
