import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return x ** 2 - y ** 2

ary = np.linspace(-5,5,50)
grid1, grid2 = np.meshgrid(ary, ary)
f_val = f(grid1, grid2)

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_surface(grid1, grid2, f_val)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title(r'$z=f(x,y)$')

fig.savefig('fig4.eps')
