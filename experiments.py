from simulator import Simulator
from simulator_log import logs_to_sbp_by_node, logs_to_ffbi_avg, logs_to_global_forks_avg, logs_to_meeting_percentage, \
    logs_to_node_ffbi_lists_list
from system_generator import SystemGenerator
from topologies import *


def run_experiments():
    simulator = Simulator()
    systems = SystemGenerator(g9, [g9_p1], [2016], [600.], g9_name)
    system = next(systems.generate())
    # data for graph 1
    logs = simulator.run_system(experiment_name='10_nodes_clique_0_propagation_powers_of_2',
                                iterations=3000000, reps=10, verbose=True, system=system)
    sbp_avg_by_node_list = logs_to_sbp_by_node(logs)
    print("# data for graph 1")
    print(sbp_avg_by_node_list)
    # data for graphs 2 + 4
    list_target_block_creation_rates = [1000., 2000., 3000., 4000., 5000., 6000., 7000., 8000., 9000., 10000.]
    systems = SystemGenerator(g3, [g3_p1], [99999999], list_target_block_creation_rates, g3_name)
    list_creation_rate_dist_ratio = [rate / g3[0][1] for rate in list_target_block_creation_rates]
    list_x_ratio_y_ffbi = []
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(
            experiment_name='2_nodes_very_far_equal_powers_constant_difficulty',
            iterations=3000000, reps=10, verbose=True, system=sys)
        ffbi_avg = logs_to_ffbi_avg(logs)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_ffbi.append((list_creation_rate_dist_ratio[i], ffbi_avg))
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graphs 2 + 4")
    print(list_x_ratio_y_ffbi)
    print(list_x_ratio_y_forks_count)

    # data for graph 3 + 5
    systems = SystemGenerator(g3, [g3_p1], [2016], list_target_block_creation_rates, g3_name)
    list_x_ratio_y_ffbi = []
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='2_nodes_very_far_equal_powers_updated_difficulty',
                                 iterations=3000000, reps=10, verbose=True, system=sys)
        ffbi_avg = logs_to_ffbi_avg(logs)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_ffbi.append((list_creation_rate_dist_ratio[i], ffbi_avg))
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graphs 3 + 5")
    print(list_x_ratio_y_ffbi)
    print(list_x_ratio_y_forks_count)

    # data for graph 6
    systems = SystemGenerator(g10, [g10_p1], [99999999], list_target_block_creation_rates, g10)
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_clique_equal_propagation_equal_powers_constant_difficulty',
                                 iterations=3000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 6")
    print(list_x_ratio_y_forks_count)

    # data for graph 7
    systems = SystemGenerator(g10, [g10_p1], [2016], list_target_block_creation_rates, g10)
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_clique_equal_propagation_equal_powers_updated_difficulty',
                                 iterations=3000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 7")
    print(list_x_ratio_y_forks_count)

    # data for graph 8 + 10
    systems = SystemGenerator(g3, [g3_p1], [9999999], [10000.], g9_name)
    system = next(systems.generate())
    list_x_iterations_num_y_forks_count = []
    list_x_iterations_num_y_meeting_percentage_list = []
    for iters in range(500000, 8500000 + 1000000, 1000000):
        logs  = simulator.run_system(experiment_name='2_nodes_very_far_equal_powers_constant_difficulty',
                                     iterations=iters, reps=10, verbose=True, system=system)
        global_forks_avg = logs_to_global_forks_avg(logs)
        meeting_percentage = logs_to_meeting_percentage(logs)
        list_x_iterations_num_y_meeting_percentage_list.append((iters, meeting_percentage))
        list_x_iterations_num_y_forks_count.append((iters, global_forks_avg))
    print("# data for graph 8")
    print(list_x_iterations_num_y_meeting_percentage_list)
    print("# data for graph 10")
    print(list_x_iterations_num_y_forks_count)

    # data for graph 9 + 11
    systems = SystemGenerator(g3, [g3_p1], [2016], [10000.], g9_name)
    system = next(systems.generate())
    list_x_iterations_num_y_forks_count = []
    list_x_iterations_num_y_meeting_percentage_list = []
    for iters in range(500000, 8500000 + 1000000, 1000000):
        logs = simulator.run_system(experiment_name='2_nodes_very_far_equal_powers_updated_difficulty',
                                    iterations=iters, reps=10, verbose=True, system=system)
        global_forks_avg = logs_to_global_forks_avg(logs)
        meeting_percentage = logs_to_meeting_percentage(logs)
        list_x_iterations_num_y_meeting_percentage_list.append((iters, meeting_percentage))
        list_x_iterations_num_y_forks_count.append((iters, global_forks_avg))
    print("# data for graph 9")
    print(list_x_iterations_num_y_meeting_percentage_list)
    print("# data for graph 11")
    print(list_x_iterations_num_y_forks_count)

    # data for graph 12
    list_target_block_creation_rates = [1000., 3000., 6000., 9000., 12000., 15000., 18000., 21000., 24000., 27000.]
    list_creation_rate_dist_ratio = [rate / g1[0][1] for rate in list_target_block_creation_rates]
    systems = SystemGenerator(g1, [g1_p1], [2016], list_target_block_creation_rates, g1_name)
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        print("12: {}".format(i))
        logs = simulator.run_system(experiment_name='10_nodes_string_equal_power_updated_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 12")
    print(list_x_ratio_y_forks_count)

    # data for graph 13
    systems = SystemGenerator(g1, [g1_p1], [999999], list_target_block_creation_rates, g1_name)
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        print("13: {}".format(i))
        logs = simulator.run_system(experiment_name='10_nodes_string_equal_power_constant_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 13")
    print(list_x_ratio_y_forks_count)

    # data for graph 14
    systems = SystemGenerator(g6, [g6_p1], [2016], list_target_block_creation_rates, g6_name)
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_cycle_equal_power_updated_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 14")
    print(list_x_ratio_y_forks_count)

    # data for graph 15
    systems = SystemGenerator(g6, [g6_p1], [999999], list_target_block_creation_rates, g6_name)
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_cycle_equal_power_constant_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 15")
    print(list_x_ratio_y_forks_count)

    # data for graph 16
    systems = SystemGenerator(g10, [g10_p2], [2016], list_target_block_creation_rates, g10_name)
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_clique_equal_power_one_dominant_updated_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 16")
    print(list_x_ratio_y_forks_count)

    # data for graph 17
    systems = SystemGenerator(g10, [g10_p2], [999999], list_target_block_creation_rates, g10_name)
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_clique_equal_power_one_dominant_constant_difficulty',
                                 iterations=500000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 17")
    print(list_x_ratio_y_forks_count)

    # data for graph 18
    power_lists = []
    for i in range(10):
        p_l = g10_p1.copy()
        p_l[0] *= g10_p1[0] * (2 ** i)
        power_lists.append(p_l)
    systems = SystemGenerator(g10, power_lists, [2016], [5000.], g10_name)
    list_x_dominant_node_normal_node_power_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_clique_equal_power_one_dominant_updated_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_dominant_node_normal_node_power_ratio_y_forks_count.append(
            (power_lists[i][0] / power_lists[i][1], global_forks_avg))
        i += 1
    print("# data for graph 18")
    print(list_x_dominant_node_normal_node_power_ratio_y_forks_count)

    # data for graph 19
    power_lists = []
    for i in range(10):
        p_l = g10_p1.copy()
        p_l[0] *= g10_p1[0] * (2 ** i)
        power_lists.append(p_l)
    systems = SystemGenerator(g10, power_lists, [999999], [5000.], g10_name)
    list_x_dominant_node_normal_node_power_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_clique_equal_power_one_dominant_constant_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_dominant_node_normal_node_power_ratio_y_forks_count.append(
            (power_lists[i][0] / power_lists[i][1], global_forks_avg))
        i += 1
    print("# data for graph 19")
    print(list_x_dominant_node_normal_node_power_ratio_y_forks_count)

    # data for graph 20
    systems = SystemGenerator(g11, [g11_p1], [2016], list_target_block_creation_rates, g11_name)
    list_creation_rate_dist_ratio = [rate / g11[0][1] for rate in list_target_block_creation_rates]
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_star_equal_power_updated_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 20")
    print(list_x_ratio_y_forks_count)

    # data for graph 21
    systems = SystemGenerator(g11, [g11_p1], [999999], list_target_block_creation_rates, g11_name)
    list_creation_rate_dist_ratio = [rate / g11[0][1] for rate in list_target_block_creation_rates]
    list_x_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_star_equal_power_constant_difficulty',
                                 iterations=500000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_ratio_y_forks_count.append((list_creation_rate_dist_ratio[i], global_forks_avg))
        i += 1
    print("# data for graph 21")
    print(list_x_ratio_y_forks_count)

    # data for graph 22
    power_lists = []
    for i in range(10):
        p_l = g11_p1.copy()
        p_l[0] *= g11_p1[0] * (2 ** i)
        power_lists.append(p_l)
    systems = SystemGenerator(g11, power_lists, [2016], [5000.], g11_name)
    list_x_dominant_node_normal_node_power_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_star_equal_power_one_dominant_updated_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_dominant_node_normal_node_power_ratio_y_forks_count.append(
            (power_lists[i][0] / power_lists[i][1], global_forks_avg))
        i += 1
    print("# data for graph 22")
    print(list_x_dominant_node_normal_node_power_ratio_y_forks_count)

    # data for graph 23
    systems = SystemGenerator(g11, power_lists, [999999], [5000.], g11_name)
    list_x_dominant_node_normal_node_power_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_star_equal_power_one_dominant_constant_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_dominant_node_normal_node_power_ratio_y_forks_count.append(
            (power_lists[i][0] / power_lists[i][1], global_forks_avg))
        i += 1
    print("# data for graph 23")
    print(list_x_dominant_node_normal_node_power_ratio_y_forks_count)

    # data for graph 24
    power_lists = []
    for i in range(10):
        p_l = g11_p1.copy()
        p_l[1] *= g11_p1[1] * (2 ** i)
        power_lists.append(p_l)
    systems = SystemGenerator(g11, power_lists, [2016], [5000.], g11_name)
    list_x_dominant_node_normal_node_power_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_star_equal_power_one_dominant_updated_difficulty',
                                 iterations=500000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_dominant_node_normal_node_power_ratio_y_forks_count.append(
            (power_lists[i][1] / power_lists[i][1], global_forks_avg))
        i += 1
    print("# data for graph 24")
    print(list_x_dominant_node_normal_node_power_ratio_y_forks_count)

    # data for graph 25
    systems = SystemGenerator(g11, power_lists, [999999], [5000.], g11_name)
    list_x_dominant_node_normal_node_power_ratio_y_forks_count = []
    i = 0
    for sys in systems.generate():
        logs = simulator.run_system(experiment_name='10_nodes_star_equal_power_one_dominant_constant_difficulty',
                                 iterations=5000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_dominant_node_normal_node_power_ratio_y_forks_count.append(
            (power_lists[i][1] / power_lists[i][1], global_forks_avg))
        i += 1
    print("# data for graph 25")
    print(list_x_dominant_node_normal_node_power_ratio_y_forks_count)

    # data for graph 26
    systems = SystemGenerator(g12, [g12_p1], [2016], [5000.], g12_name)
    system = next(systems.generate())
    list_x_iterations_num_y_dominant_clique_meeting_percentage_list = []
    for iters in range(500000, 10000000 + 2000000, 2000000):
        logs = simulator.run_system(
            experiment_name='5_nodes_clique_zero_distance_equal_powers_one_far_dominant_constant_difficulty',
            iterations=iters, reps=20, verbose=True, system=system)
        node_ffbi_lists_list = logs_to_node_ffbi_lists_list(logs)
        meets_num = len([_ for node_ffbi_list in node_ffbi_lists_list if node_ffbi_list[5][1] != -1])
        percentage = 100. * float(meets_num) / float(len(node_ffbi_lists_list))
        list_x_iterations_num_y_dominant_clique_meeting_percentage_list.append((iters, percentage))
    print("# data for graph 26")
    print(list_x_iterations_num_y_dominant_clique_meeting_percentage_list)

    # data for graph 27
    systems = SystemGenerator(g12, [g12_p1], [999999], [5000.], g12_name)
    system = next(systems.generate())
    list_x_iterations_num_y_dominant_clique_meeting_percentage_list = []
    for iters in range(500000, 10000000 + 2000000, 2000000):
        logs = simulator.run_system(
            experiment_name='5_nodes_clique_zero_distance_equal_powers_one_far_dominant_constant_difficulty',
            iterations=iters, reps=20, verbose=True, system=system)
        node_ffbi_lists_list = logs_to_node_ffbi_lists_list(logs)
        meets_num = len([_ for node_ffbi_list in node_ffbi_lists_list if node_ffbi_list[5][1] != -1])
        percentage = 100. * float(meets_num) / float(len(node_ffbi_lists_list))
        list_x_iterations_num_y_dominant_clique_meeting_percentage_list.append((iters, percentage))
    print("# data for graph 27")
    print(list_x_iterations_num_y_dominant_clique_meeting_percentage_list)

    # data for graphs 40 + 41
    list_target_block_creation_rates = [6000.]
    epoch_sizes = list(range(1000, 90000 + 1000, 10000))
    systems = SystemGenerator(g3, [g3_p1], epoch_sizes, list_target_block_creation_rates, g3_name)
    list_x_epoch_size_y_ffbi = []
    list_x_epoch_size_y_forks_count = []
    i = 0
    for sys in systems.generate():
        print(i)
        logs = simulator.run_system(
            experiment_name='2_nodes_equal_powers_constant_difficulty',
            iterations=1000000, reps=10, verbose=True, system=sys)
        ffbi_avg = logs_to_ffbi_avg(logs)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_epoch_size_y_ffbi.append((epoch_sizes[i], ffbi_avg))
        list_x_epoch_size_y_forks_count.append((epoch_sizes[i], global_forks_avg))
        i += 1
    print("# data for graphs 40")
    print(list_x_epoch_size_y_ffbi)
    print("# data for graphs 41")
    print(list_x_epoch_size_y_forks_count)

    # data for graphs 42
    list_target_block_creation_rates = [6000.]
    epoch_sizes = list(range(1000, 25000 + 2500, 2500))
    systems = SystemGenerator(g10, [g10_p1], epoch_sizes, list_target_block_creation_rates, g10_name)
    list_x_epoch_size_y_forks_count = []
    i = 0
    for sys in systems.generate():
        print(i)
        logs = simulator.run_system(
            experiment_name='2_nodes_equal_powers_constant_difficulty',
            iterations=2000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_epoch_size_y_forks_count.append((epoch_sizes[i], global_forks_avg))
        i += 1
    print("# data for graphs 42")
    print(list_x_epoch_size_y_forks_count)

    # data for graphs 43
    list_target_block_creation_rates = [6000.]
    epoch_sizes = list(range(1000, 90000 + 1000, 10000))
    systems = SystemGenerator(g6, [g6_p1], epoch_sizes, list_target_block_creation_rates, g6_name)
    list_x_epoch_size_y_forks_count = []
    i = 0
    for sys in systems.generate():
        print(i)
        logs = simulator.run_system(
            experiment_name='2_nodes_equal_powers_constant_difficulty',
            iterations=2000000, reps=10, verbose=True, system=sys)
        global_forks_avg = logs_to_global_forks_avg(logs)
        list_x_epoch_size_y_forks_count.append((epoch_sizes[i], global_forks_avg))
        i += 1
    print("# data for graphs 43")
    print(list_x_epoch_size_y_forks_count)