import numpy as np

array1 = np.array([1,2,3,4])
array2 = np.array([-1,-2,-3,-4])

matrix = np.c_[array1, array2]

print('matrix=\n{},\nshape={}'.format(matrix, matrix.shape))
