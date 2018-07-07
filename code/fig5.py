import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return ( np.exp(x) + np.exp(-x) + np.exp(y) + np.exp(-y) ) / 4

ary = np.linspace(-5,5,50)
grid1, grid2 = np.meshgrid(ary, ary)
f_val = f(grid1, grid2)

fig = plt.figure(figsize=(15,5))

ax1 = fig.add_subplot(1,3,1, projection='3d')
ax1.plot_surface(grid1, grid2, f_val)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

ax2 = fig.add_subplot(1,3,2)
ax2.contour(grid1, grid2, f_val)
ax2.set_xlabel('x')
ax2.set_ylabel('y')

ax3 = fig.add_subplot(1,3,3)
ax3.contour(grid1, grid2, f_val, levels=np.logspace(0,5,11,base=np.e))
ax3.set_xlabel('x')
ax3.set_ylabel('y')

fig.savefig('fig5.eps')
