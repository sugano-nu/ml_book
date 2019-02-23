import numpy as np

scl = 3
array_1d_scl = np.array([3])
array_2d_scl = np.array([[3]])

print('scalar={}, type={}'.format(scl,type(scl)))
print('array_1d_scl={}, type={}, shape={}'.format(array_1d_scl,type(array_1d_scl),
                                                    array_1d_scl.shape))
print('array_2d_scl={}, type={}, shape={}'.format(array_2d_scl,type(array_2d_scl),
                                                    array_2d_scl.shape))

print('array_1d_scl[0]={}, type={}'.format(array_1d_scl[0],type(array_1d_scl[0])))
print('array_2d_scl[0]={}, type={}, shape={}'.format(array_2d_scl[0],
                                                type(array_2d_scl[0]),array_2d_scl[0].shape))
print('array_2d_scl[0,0]={}, type={}'.format(array_2d_scl[0,0],type(array_2d_scl[0,0])))
