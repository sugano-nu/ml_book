import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,8,10])
y = np.array([-3,5,-2,3])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')

fig.savefig('fig3.eps')
