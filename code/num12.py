import numpy as np

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
B = np.array([[-1,-2,-3,-4]])
C = np.array([[-1],[-2],[-3],[-4]])
d = np.array([-1,-2,-3,-4])
s = 100

print('A + B=\n{}'.format(A + B))
print('A * C=\n{}'.format(A * C))
print('A + d=\n{}'.format(A / d))
print('A + s=\n{}'.format(A + s))
