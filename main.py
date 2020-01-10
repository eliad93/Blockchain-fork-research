from system_generator import SystemGenerator
from topologies import *
from simulator import Simulator


def main():
    simulator = Simulator()
    # systems = SystemGenerator(g9, [g9_p1], [2016], [600.], g9_name)
    # system = next(systems.generate())
    # # data for graph 1
    # _, sbp_avg_by_node_list, _ = simulator.run_system(experiment_name='10_nodes_clique_0_propagation_powers_of_2',
    #                                                   iterations=3000000, reps=3, verbose=True, system=system)
    # print("# data for graph 1")
    # print(sbp_avg_by_node_list)
    # data for graphs 2 + 4
    list_target_block_creation_rates = [1000., 2000., 3000., 4000., 5000., 6000., 7000., 8000., 9000., 10000.]
    # systems = SystemGenerator(g3, [g3_p1], [99999999], list_target_block_creation_rates, g3_name)
    list_creation_rate_dist_ratio = [rate / g3[0][1] for rate in list_target_block_creation_rates]
    # list_x_ratio_y_ffbi = []
    # list_x_ratio_y_forks_count = []
    # i = 0
    # for sys in systems.generate():
    #     ffbi_avg, _, global_forks_avg = simulator.run_system(
    #         experiment_name='2_nodes_very_far_equal_powers_constant_difficulty',
    #         iterations=3000000, reps=10, verbose=True, system=sys)
    #     list_x_ratio_y_ffbi.append((list_creation_rate_dist_ratio[i], ffbi_avg))
    #     list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
    #     i += 1
    # print("# data for graphs 2 + 4")
    # print(list_x_ratio_y_ffbi)
    # print(list_x_ratio_y_forks_count)
    # # todo: export to csv
    #
    # # data for graph 3 + 5
    # systems = SystemGenerator(g3, [g3_p1], [2016], list_target_block_creation_rates, g3_name)
    # list_x_ratio_y_ffbi = []
    # list_x_ratio_y_forks_count = []
    # i = 0
    # for sys in systems.generate():
    #     ffbi_avg, _, global_forks_avg = \
    #         simulator.run_system(experiment_name='2_nodes_very_far_equal_powers_updated_difficulty',
    #                              iterations=3000000, reps=10, verbose=True, system=sys)
    #     list_x_ratio_y_ffbi.append((list_creation_rate_dist_ratio[i], ffbi_avg))
    #     list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
    #     i += 1
    # print("# data for graphs 3 + 5")
    # print(list_x_ratio_y_ffbi)
    # print(list_x_ratio_y_forks_count)
    # # todo: export to csv

    # # data for graph 6
    # systems = SystemGenerator(g10, [g10_p1], [99999999], list_target_block_creation_rates, g10)
    # list_x_ratio_y_forks_count = []
    # i = 0
    # for sys in systems.generate():
    #     _, _, global_forks_avg = \
    #         simulator.run_system(experiment_name='10_nodes_clique_equal_propagation_equal_powers_constant_difficulty',
    #                              iterations=3000000, reps=3, verbose=True, system=sys)
    #     list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
    #     i += 1
    # print("# data for graph 6")
    # print(list_x_ratio_y_forks_count)
    # # todo: export to csv
    #
    # # data for graph 7
    # systems = SystemGenerator(g10, [g10_p1], [2016], list_target_block_creation_rates, g10)
    # list_x_ratio_y_forks_count = []
    # i = 0
    # for sys in systems.generate():
    #     _, _, global_forks_avg = \
    #         simulator.run_system(experiment_name='10_nodes_clique_equal_propagation_equal_powers_updated_difficulty',
    #                              iterations=3000000, reps=3, verbose=True, system=sys)
    #     list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
    #     i += 1
    # print("# data for graph 7")
    # print(list_x_ratio_y_forks_count)
    # # todo: export to csv

    # data for graph 8 + 10
    systems = SystemGenerator(g3, [g3_p1], [9999999], [600.], g9_name)
    system = next(systems.generate())
    list_x_ratio_y_forks_count = []
    list_x_iterations_num_y_meeting_percentage_list = []
    for i, iters in enumerate(range(300000, 1500000, 1500000 + 300000)):
        _, _, global_forks_avg, meeting_percentage = simulator.run_system(experiment_name='2_nodes_very_far_equal_powers_constant_difficulty',
                                                          iterations=iters, reps=10, verbose=True, system=system)
        list_x_iterations_num_y_meeting_percentage_list.append((iters, meeting_percentage))
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
    print("# data for graph 8")
    print(list_x_iterations_num_y_meeting_percentage_list)
    print("# data for graph 10")
    print(list_x_ratio_y_forks_count)

    # data for graph 9 + 11
    systems = SystemGenerator(g3, [g3_p1], [2016], [600.], g9_name)
    system = next(systems.generate())
    list_x_ratio_y_forks_count = []
    list_x_iterations_num_y_meeting_percentage_list = []
    for i, iters in enumerate(range(300000, 1500000, 1500000 + 300000)):
        _, _, global_forks_avg, meeting_percentage = simulator.run_system(experiment_name='2_nodes_very_far_equal_powers_updated_difficulty',
                                                          iterations=iters, reps=10, verbose=True, system=system)
        list_x_iterations_num_y_meeting_percentage_list.append((iters, meeting_percentage))
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
    print("# data for graph 9")
    print(list_x_iterations_num_y_meeting_percentage_list)
    print("# data for graph 11")
    print(list_x_ratio_y_forks_count)


if __name__ == "__main__":
    main()
