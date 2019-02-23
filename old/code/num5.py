import numpy as np

array_1d = np.array([1,2,3,4,5])
array_2d = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print('array_1d[1::2]=\n{}'.format(array_1d[1::2]))
print('array_2d[::2,::2]=\n{}'.format(array_2d[::2,::2]))
print('array_2d[3]=\n{},shape={}'.format(array_2d[3],array_2d[3].shape))
print('array_2d[:,1]=\n{},shape={}'.format(array_2d[:,1],array_2d[:,1].shape))
print('array_2d[0,0]=\n{}'.format(array_2d[0,0]))
