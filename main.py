from blockchain_simulator import SystemProperties, System
from events import BlockCreation, BlockArrival

import queue as Q

string_unified_3 = [[0, 1, -1], [1, 0, 1], [-1, 1, 0]]
power_dict = {1, 1, 1}


def main():
    prop1 = SystemProperties(string_unified_3, power_dict, 1, 100, 1)
    system1 = System(prop1)
    b1 = BlockCreation(5, 1)
    b2 = BlockCreation(7, 2)
    b3 = BlockArrival(6, 3, 1)
    b4 = BlockArrival(4, 4, 2)
    q = Q.PriorityQueue()
    q.put(b1)
    q.put(b2)
    q.put(b3)
    q.put(b4)
    print(q.get().timestamp)


if __name__ == "__main__":
    main()
