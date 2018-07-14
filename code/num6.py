import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
B = np.array([[1,2],[3,4],[5,6]])
C1 = np.array([[1],[2]])
C2 = np.array([[3],[4]])
D = np.array([[1,2,3,4]])
E = np.array([[-6,5],[4,-3],[-2,1]])

F = A.dot(B).dot(C1).dot(D)
G = D.dot(A.dot(B).dot(C1 + C2))
H = B * E

I = np.array([[1,1],[1,1],[1,1]])
J = np.linalg.pinv(I)

print('F=\n{}'.format(F))
print('G=\n{}'.format(G))
print('H=\n{}'.format(H))
print('J=\n{}'.format(J))
