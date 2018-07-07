import numpy as np

ary = np.array([0,1,2])

grid = np.meshgrid(ary, ary)
print('grid=\n{}\ntype={}'.format(grid, type(grid)))

grid1, grid2 = np.meshgrid(ary, ary)
grid1 = grid1.flatten()
grid2 = grid2.flatten()
grid = np.c_[grid1, grid2]
print('grid=\n{}\ntype={}'.format(grid, type(grid)))
