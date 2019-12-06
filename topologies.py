# string of 10 nodes
g1 = [[0., 1., -1., -1., -1., -1., -1., -1., -1., -1.],
      [1., 0., 1., -1., -1., -1., -1., -1., -1., -1.],
      [-1., 1., 0., 1., -1., -1., -1., -1., -1., -1.],
      [-1., -1., 1., 0., 1., -1., -1., -1., -1., -1.],
      [-1., -1., -1., 1., 0., 1., -1., -1., -1., -1.],
      [-1., -1., -1., -1., 1., 0., 1., -1., -1., -1.],
      [-1., -1., -1., -1., -1., 1., 0., 1., -1., -1.],
      [-1., -1., -1., -1., -1., -1., 1., 0., 1., -1.],
      [-1., -1., -1., -1., -1., -1., -1., 1., 0., 1.],
      [-1., -1., -1., -1., -1., -1., -1., -1., 1., 0.]]

g1_p1 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

# 2 separated strings of 7 nodes connected in the middle
g2 = [[0., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
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

g2_p1 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

# 2 nodes with big and symmetric propagation time
g3 = [[0., 999999.],
      [999999., 0.]]

g3_p1 = [1., 1.]

g3_p2 = [1., 1.01]

g3_p3 = [1., 2.]

# 20 nodes clique with small propagation time
g4 = [[0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
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

g4_p1 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

g4_p2 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 2., 2., 2., 2., 2., 2., 2., 2., 2., 2.]

# 20 nodes clique with no propagation time
g5 = [[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
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

g5_p1 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

g5_p2 = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20.]

# 10 nodes cycle
g6 = [[0., 1., -1., -1., -1., -1., -1., -1., -1., 1.],
      [1., 0., 1., -1., -1., -1., -1., -1., -1., -1.],
      [-1., 1., 0., 1., -1., -1., -1., -1., -1., -1.],
      [-1., -1., 1., 0., 1., -1., -1., -1., -1., -1.],
      [-1., -1., -1., 1., 0., 1., -1., -1., -1., -1.],
      [-1., -1., -1., -1., 1., 0., 1., -1., -1., -1.],
      [-1., -1., -1., -1., -1., 1., 0., 1., -1., -1.],
      [-1., -1., -1., -1., -1., -1., 1., 0., 1., -1.],
      [-1., -1., -1., -1., -1., -1., -1., 1., 0., 1.],
      [1., -1., -1., -1., -1., -1., -1., -1., 1., 0.]]

g6_p1 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

g6_p2 = [9., 1., 1., 1., 1., 9., 1., 1., 1., 1.]

# 2 connected cycles with 6 nodes each (1 shared node)
g7 = [[0., 1., -1., -1., -1., 1., -1., -1., -1., -1., -1.],
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

g7_p1 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]

# 2-regular bipartite graph with 10 nodes at each side
g8 = [[0., -1., -1., -1., -1., -1., -1., -1., -1., -1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1.],
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

g8_p1 = [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]
