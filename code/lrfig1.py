import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = np.array([1,2,3])
y = x

ax.scatter(x, y)

ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')

fig.savefig('lrfig1.eps')
