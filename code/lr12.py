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
        theta_hist[i+1] = theta.flatten()
    return theta, theta_hist, J_hist

def hypo_function(X, theta):
    y_pred = X.dot(theta)
    return y_pred

df = pd.read_csv('../data/ex1data2.txt', names=['area','bedroom','price'])

df['all_1'] = 1
X = df[['all_1','area','bedroom']].values
y = df['price'].values
y = np.c_[y]

ALPHA = 0.00000003
ITERA = 50
THETA = np.array([[0],[0],[0]])

theta, theta_hist, J_hist = gradient_descent(X, y, THETA, ALPHA, ITERA)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(np.arange(ITERA+1), J_hist)
ax.set_xlabel('iter')
ax.set_ylabel(r'$J(\theta)$')

fig.savefig('lrfig9.eps')

X_pred = np.array([[1,2500,3]])
y_pred = hypo_function(X_pred, theta)

print('y_pred={}'.format(y_pred[0,0]))
