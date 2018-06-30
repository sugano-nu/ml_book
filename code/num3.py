import numpy as np

lst_1d = [1,3,5,9]
array_1d = np.array(lst_1d)
print('array_1d=\n{}\nshape={}\ntype={}\n'.format(array_1d, array_1d.shape, type(array_1d)))

lst_cv = [[1],[3],[5],[9]]
array_cv = np.array(lst_cv)
print('array_cv=\n{}\nshape={}\ntype={}\n'.format(array_cv,array_cv.shape, type(array_cv)))

lst_rv = [[1,3,5,9]]
array_rv = np.array(lst_rv)
print('array_cv=\n{}\nshape={}\ntype={}\n'.format(array_rv,array_rv.shape, type(array_rv)))


array_1d_modc = np.c_[array_1d]
print('array_1d_modc=\n{}\nshape={}\ntype={}\n'.format(array_1d_modc,
                                    array_1d_modc.shape, type(array_1d_modc)))

array_1d_modr = np.c_[array_1d].T
print('array_1d_modr=\n{}\nshape={}\ntype={}\n'.format(array_1d_modr,
                                    array_1d_modr.shape, type(array_1d_modr)))
