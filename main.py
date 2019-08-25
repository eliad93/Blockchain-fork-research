from blockchain_simulator import SystemProperties, System

graph1 = [[0, 1, -1],
          [1, 0, 1],
          [-1, 1, 0]]
power_list1 = [1, 1, 1]

graph2 = [[0, 6, 17, -1, -1, 100],
          [6, 0, 13, -1, -1, -1],
          [17, 13, 0, -1, -1, -1],
          [-1, -1, -1, 0, 3, 29],
          [-1, -1, -1, 3, 0, 47],
          [100, -1, -1, 29, 47, 0]]

power_list2 = [2, 4, 8, 16, 32, 64]


def main():
    prop = SystemProperties(graph2, power_list2, 2016, 600)
    system = System(prop)
    for i in range(5000):
        system.step()
    system.print_nodes_ledgers()


if __name__ == "__main__":
    main()
