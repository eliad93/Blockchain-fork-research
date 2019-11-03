# string of 10 nodes
graph1 = [[0., 1., -1., -1., -1., -1., -1., -1., -1., -1.],
          [1., 0., 1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., 1., 0., 1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., 1., 0., 1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., 1., 0., 1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., 1., 0., 1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., 1., 0., 1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., 1., 0., 1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., 1., 0., 1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., 1., 0.]]

power_list1 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

# 2 strings of 7 nodes connected in the middle
graph2 = [[0., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
          [1., 0., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., 1., 0., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., 1., 0., 1., -1., -1., -1., -1., -1., 1., -1., -1., -1.],
          [-1., -1., -1., 1., 0., 1., -1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., 1., 0., 1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., 1., 0., -1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., 0., 1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., 1., 0., 1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., 1., 0., 1., -1., -1., -1.],
          [-1., -1., -1., 1., -1., -1., -1., -1., -1., 1., 0., 1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 0., 1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 0., 1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 0.]]

power_list2 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

# 2 nodes with big and symmetric propagation time
graph3 = [[0., 999999.],
          [999999., 0.]]

power_list3 = [1., 1.]

power_list4 = [1., 1.01]

power_list5 = [1., 2.]

# 20 connected nodes with small propagation time
graph4 = [[0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 1.],
          [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0.]]

power_list6 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

power_list7 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2.]

# 20 connected nodes with no propagation time
graph5 = [[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]

power_list8 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

power_list9 = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20.]

# 10 nodes cycle
graph6 = [[0., 1., -1., -1., -1., -1., -1., -1., -1., 1.],
          [1., 0., 1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., 1., 0., 1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., 1., 0., 1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., 1., 0., 1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., 1., 0., 1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., 1., 0., 1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., 1., 0., 1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., 1., 0., 1.],
          [1., -1., -1., -1., -1., -1., -1., -1., 1., 0.]]

power_list10 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

power_list11 = [9., 1., 1., 1., 1., 9., 1., 1., 1., 1.]

# 2 connected cycles with 6 nodes each (1 shared node)
graph7 = [[0., 1., -1., -1., -1., 1., -1., -1., -1., -1., -1.],
          [1., 0., 1., -1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., 1., 0., 1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., 1., 0., 1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., 1., 0., 1., -1., -1., -1., -1., -1.],
          [1., -1., -1., -1., 1., 0., 1., -1., -1., -1., 1.],
          [-1., -1., -1., -1., -1., 1., 0., 1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., 1., 0., 1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., 1., 0., 1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., 1., 0., 1.],
          [-1., -1., -1., -1., -1., 1., -1., -1., -1., 1., 0.]]

power_list12 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

# 2-regular bipartite graph with 10 nodes at each side
graph8 = [[0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., -1., 0., 1., -1., -1., -1., -1., -1., -1., -1., -1., 1.],
          [1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 0., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
          [1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0., -1., -1., -1., -1., -1., -1., -1., -1.],
          [-1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0., -1., -1., -1., -1., -1., -1., -1.],
          [-1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0., -1., -1., -1., -1., -1., -1.],
          [-1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0., -1., -1., -1., -1., -1.],
          [-1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0., -1., -1., -1., -1.],
          [-1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0., -1., -1., -1.],
          [-1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0., -1., -1.],
          [-1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0., -1.],
          [-1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., 0.]]

power_list13 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]