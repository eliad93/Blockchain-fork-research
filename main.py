from system_generator import SystemGenerator
from topologies import *
from simulator import Simulator
from system import System, SystemProperties
from simulator_log import SimulatorLog


def main():
    props4 = SystemProperties(graph3, power_list3, 99999999999999999, 600.)
    system4 = System(4, props4)
    systems = SystemGenerator(graph3, [power_list3], [99999999999999999],
                              [600.], 4)
    simulator = Simulator(systems)
    simulator.hyper_run(experiment_name="try3", iterations=30000,
                        block_arrivals_per_snapshot=500, reps=10,
                        verbose=True)


if __name__ == "__main__":
    main()
