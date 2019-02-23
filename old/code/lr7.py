import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(X, y, theta, alpha, itera):
    m, n = X.shape
    for i in range(itera):
        J_grad = 1 / m * (X.T.dot(X).dot(theta) - X.T.dot(y))
        theta = theta - alpha * J_grad
    return theta

def hypo_function(X, theta):
    y_pred = X.dot(theta)
    return y_pred

df = pd.read_csv('../data/ex1data1.txt', names=['population','profit'])

df['all_1'] = 1
X = df[['all_1','population']].values
y = df['profit'].values
y = np.c_[y]

ALPHA = 0.01
ITERA = 1500
THETA = np.array([[1],[-2]])

theta = gradient_descent(X, y, THETA, ALPHA, ITERA)
y_pred = hypo_function(X, theta)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.grid()
ax.scatter(df['population'].values, y.flatten())
ax.set_xlabel('Population of City in 10,000s')
ax.set_ylabel('Profit in $10,000s')
ax.plot(df['population'].values, y_pred.flatten())

fig.savefig('lrfig4.eps')
