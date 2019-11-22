from topologies import *
from simulator import Simulator
from system import System, SystemProperties
from simulator_log import SimulatorLog


def main():
    # props1 = SystemProperties(graph1, power_list1, 2016, 600.)
    # system1 = System(1, props1)
    # props2 = SystemProperties(graph2, power_list2, 2016, 600.)
    # system2 = System(2, props2)
    # props3 = SystemProperties(graph3, power_list3, 100, 600.)
    # system3 = System(3, props3)
    props4 = SystemProperties(graph3, power_list3, 99999999999999999, 600.)
    system4 = System(4, props4)
    # props5 = SystemProperties(graph4, power_list4, 100, 600.)
    # system5 = System(5, props5)
    # props6 = SystemProperties(graph5, power_list4, 100, 600.)
    # system6 = System(6, props6)
    # for i in range(3000):
    # system1.step()
    # system2.step()
    # system3.step()
    # system4.step()
    # system5.step()
    # system6.step()
    # system1.print_nodes_ledgers()
    # system2.print_nodes_ledgers()
    # system3.print_nodes_ledgers()
    # system4.print_nodes_ledgers()
    # system4.print_nodes_accepted_blocks()
    # system5.print_nodes_ledgers()
    # system6.print_nodes_ledgers()
    # log = SimulatorLog(props4.get_number_of_nodes(), "try")
    # log.snapshot_blockchains(system4.nodes)
    simulator = Simulator(system4)
    simulator.run_simulation(experiment_name="try3", iterations=3000000,
                             block_arrivals_per_snapshot=5000, reps=10,
                             verbose=True)


if __name__ == "__main__":
    main()
