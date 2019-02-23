import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def cost_function(X, y, theta):
    m, n = X.shape
    J = 1 / (2 * m) * (X.dot(theta) - y).T.dot(X.dot(theta) - y)
    return J[0,0]

def gradient_descent(X, y, theta, alpha, itera):
    m, n = X.shape
    theta_n, dummy = theta.shape
    theta_hist = np.zeros((itera+1, theta_n))
    theta_hist[0] = theta.flatten()
    J_hist = np.zeros(itera+1)
    J_hist[0] = cost_function(X, y, theta)
    for i in range(itera):
        J_grad = 1 / m * (X.T.dot(X).dot(theta) - X.T.dot(y))
        theta = theta - alpha * J_grad
        J_hist[i+1] = cost_function(X, y, theta)
    return theta, theta_hist, J_hist

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

theta, theta_hist, J_hist = gradient_descent(X, y, THETA, ALPHA, ITERA)
y_pred = hypo_function(X, theta)

theta_ne = np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(y)
y_pred_ne = hypo_function(X, theta_ne)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.grid()
ax.scatter(df['population'].values, y.flatten())
ax.set_xlabel('Population of City in 10,000s')
ax.set_ylabel('Profit in $10,000s')
ax.plot(df['population'].values, y_pred.flatten(), label='GD')
ax.plot(df['population'].values, y_pred_ne.flatten(), label='NE')
ax.legend()

fig.savefig('lrfig8.eps')
