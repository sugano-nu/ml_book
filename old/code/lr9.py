import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gradient_descent(X, y, theta, alpha, itera):
    m, n = X.shape
    theta_n, dummy = theta.shape
    theta_hist = np.zeros((itera+1, theta_n))
    theta_hist[0] = theta.flatten()
    for i in range(itera):
        J_grad = 1 / m * (X.T.dot(X).dot(theta) - X.T.dot(y))
        theta = theta - alpha * J_grad
        theta_hist[i+1] = theta.flatten()
    return theta, theta_hist

def cost_function(X, y, theta):
    m, n = X.shape
    J = 1 / (2 * m) * (X.dot(theta) - y).T.dot(X.dot(theta) - y)
    return J[0,0]

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
THETA = np.array([[0],[0]])

theta_opt, theta_hist = gradient_descent(X, y, THETA, ALPHA, ITERA)

theta0 = np.linspace(-15, 10, 50)
theta1 = np.linspace(-1, 4, 50)
theta_grid0, theta_grid1 = np.meshgrid(theta0, theta1)
m, n = theta_grid0.shape
J_val = np.zeros((m, n))

for i in range(m):
    for j in range(n):
        theta = np.array([[theta_grid0[i,j]], [theta_grid1[i,j]]])
        J_val[i,j] = cost_function(X, y, theta)

NUM = [0,1,10,1000]
fig = plt.figure(figsize=(7, 12))

for i in range(len(NUM)):
    theta_tmp = theta_hist[NUM[i]]
    y_pred = hypo_function(X, theta_tmp)

    ax1 = fig.add_subplot(len(NUM), 2, i*2+1)
    ax1.scatter(df['population'].values, df['profit'].values)
    ax1.plot(df['population'].values, y_pred)
    ax1.set_title('iter={}'.format(NUM[i]))

    ax2 = fig.add_subplot(len(NUM), 2, i*2+2)
    ax2.contour(theta_grid0, theta_grid1, J_val, levels=np.logspace(-2, 3, 20))
    ax2.scatter(theta_tmp[0], theta_tmp[1])

fig.subplots_adjust(hspace=0.5)

fig.savefig('lrfig6.eps')
