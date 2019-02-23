import numpy as np

lst_1d = [1,3,5,9]
array_1d = np.array(lst_1d)
print('array_1d=\n{}\nshape={}\ntype={}\n'.format(array_1d, array_1d.shape, type(array_1d)))

lst_2d = [[1,3,5],[2,4,6],[3,6,9],[5,10,15]]
array_2d = np.array(lst_2d)
print('array_2d=\n{}\nshape={}\ntype={}\n'.format(array_2d, array_2d.shape, type(array_1d)))
