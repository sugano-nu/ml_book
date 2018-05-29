import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))

fig.savefig('fig2.eps')
