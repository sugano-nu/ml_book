import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = np.arange(30)
y = np.arange(30) + 3 * np.random.randn(30)

ax.scatter(x, y)
ax.plot(x, x, label='y=x')
ax.plot(x, x / 2, label='y=x/2')

ax.grid()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

fig.savefig('fig6.eps')
