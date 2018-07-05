import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def hypo_function(X, theta):
    y_pred = X.dot(theta)
    return y_pred

df = pd.read_csv('../data/ex1data1.txt', names=['population','profit'])

df['all_1'] = 1
X = df[['all_1','population']].values
y = df['profit'].values

THETA = np.array([[1],[-2]])

y_pred = hypo_function(X, THETA)
y_pred = y_pred.flatten()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.grid()
ax.scatter(df['population'].values, y)
ax.set_xlabel('Population of City in 10,000s')
ax.set_ylabel('Profit in $10,000s')

ax.plot(df['population'].values, y_pred)

fig.savefig('lrfig3.eps')
