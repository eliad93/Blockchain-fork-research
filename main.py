from blockchain_simulator import SystemProperties, System
from events import BlockCreation, BlockArrival

simple_path_with_three_nodes = [[0, 1, -1],
                                [1, 0, 1],
                                [-1, 1, 0]]
power_list = [1, 1, 1]


def main():
    prop1 = SystemProperties(simple_path_with_three_nodes, power_list, 2016, 600)
    system1 = System(prop1)
    for i in range(3000):
        system1.step()
    system1.print_nodes_ledgers()


if __name__ == "__main__":
    main()
