import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0,10,11)
y1 = x
y2 = x * 3

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(1,2,1)
ax1.plot(x, y1)
ax2 = fig.add_subplot(1,2,2)
ax2.plot(x, y2)

fig.savefig('fig8-1.eps')

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(1,2,1)
ax1.plot(x, y1)
ax2 = fig.add_subplot(1,2,2, sharey=ax1)
ax2.plot(x, y2)

fig.savefig('fig8-2.eps')
