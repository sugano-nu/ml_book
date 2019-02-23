import numpy as np

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print('A_sum_all={}'.format(A.sum()))
print('A_mean_bycol={}'.format(A.mean(axis=0)))
print('A_std_byrow={}'.format(A.std(axis=1)))
