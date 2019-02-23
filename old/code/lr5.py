import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/ex1data1.txt', names=['population','profit'])

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.grid()
ax.scatter(df['population'].values, df['profit'].values)
ax.set_xlabel('Population of City in 10,000s')
ax.set_ylabel('Profit in $10,000s')

fig.savefig('lrfig2.eps')
