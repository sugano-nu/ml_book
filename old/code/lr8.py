import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def cost_function(X, y, theta):
    m, n = X.shape
    J = 1 / (2 * m) * (X.dot(theta) - y).T.dot(X.dot(theta) - y)
    return J[0,0]

def gradient_descent(X, y, theta, alpha, itera):
    m, n = X.shape
    for i in range(itera):
        J_grad = 1 / m * (X.T.dot(X).dot(theta) - X.T.dot(y))
        theta = theta - alpha * J_grad
    return theta

df = pd.read_csv('../data/ex1data1.txt', names=['population','profit'])

df['all_1'] = 1
X = df[['all_1','population']].values
y = df['profit'].values
y = np.c_[y]

theta0 = np.linspace(-15, 10, 50)
theta1 = np.linspace(-1, 4, 50)
theta_grid0, theta_grid1 = np.meshgrid(theta0, theta1)
m, n = theta_grid0.shape
J_val = np.zeros((m, n))

for i in range(m):
    for j in range(n):
        theta = np.array([[theta_grid0[i,j]], [theta_grid1[i,j]]])
        J_val[i,j] = cost_function(X, y, theta)

fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(1,2,1, projection='3d')
ax1.plot_surface(theta_grid0, theta_grid1, J_val)
ax1.set_xlabel(r'$\theta_0$')
ax1.set_ylabel(r'$\theta_1$')
ax1.set_zlabel(r'$J(\theta)$')

ax2 = fig.add_subplot(1,2,2)
ax2.contour(theta_grid0, theta_grid1, J_val, levels=np.logspace(-2, 3, 20))
ax2.set_xlabel(r'$\theta_0$')
ax2.set_ylabel(r'$\theta_1$')

ALPHA = 0.01
ITERA = 1500
THETA = np.array([[1],[-2]])
theta_opt = gradient_descent(X, y, THETA, ALPHA, ITERA)

ax2.scatter(theta_opt[0,0], theta_opt[1,0])

fig.savefig('lrfig5.eps')
