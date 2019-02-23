import numpy as np

A = np.array([[1,2,3,4]])
B = np.array([[1],[2],[3],[4]])
C = np.array([[1,2,3],[4,5,6],[7,8,9]])
D = np.array([[3]])

print('A.flatten()=\n{}\nA.flatten().shape={}\n'.format(A.flatten(),A.flatten().shape))
print('B.flatten()=\n{}\nB.flatten().shape={}\n'.format(B.flatten(),B.flatten().shape))
print('C.flatten()=\n{}\nC.flatten().shape={}\n'.format(C.flatten(),C.flatten().shape))
print('C.flatten(F)=\n{}\nC.flatten(F).shape={}\n'.format(C.flatten('F'),
                                                        C.flatten('F').shape))
print('D.flatten()=\n{}\nD.flatten().shape={}'.format(D.flatten(),D.flatten().shape))
