from blockchain_simulator import SystemProperties, System
from events import BlockCreation, BlockArrival

import queue as Q

string_unified_3 = [[0, 1, -1], [1, 0, 1], [-1, 1, 0]]
power_list = [1, 1, 1]


def main():
    prop1 = SystemProperties(string_unified_3, power_list, 1, 100, 1)
    system1 = System(prop1)
    for i in range(100):
        system1.step()
    system1.print_nodes_ledgers()


if __name__ == "__main__":
    main()
