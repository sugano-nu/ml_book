import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

fig.subplots_adjust(wspace=0.3, hspace=0.5)

fig.savefig('fig7.eps')
