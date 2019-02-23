import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = np.arange(30)
y = np.arange(30) + 3 * np.random.randn(30)

ax.scatter(x, y)

ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')

fig.savefig('fig2.eps')
