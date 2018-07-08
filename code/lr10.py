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

df = pd.read_csv('../data/ex1data1.txt', names=['population','profit'])

df['all_1'] = 1
X = df[['all_1','population']].values
y = df['profit'].values
y = np.c_[y]

ITERA = 1500
ALPHA = [0.00001, 0.0001, 0.024324]
THETA = np.array([[0],[0]])

fig = plt.figure(figsize=(12, 4))
axs = list()
flag = 0

for i in range(len(ALPHA)):
    theta_opt, theta_hist, J_hist = gradient_descent(X, y, THETA, ALPHA[i], ITERA)
    if flag == 0:
        ax = fig.add_subplot(1, len(ALPHA), i+1)
        flag = 1
    else:
        ax = fig.add_subplot(1, len(ALPHA), i+1, sharey=axs[0])
    ax.plot(np.arange(ITERA+1), J_hist)
    ax.set_title('alpha={:f}'.format(ALPHA[i]))
    ax.set_xlabel('iter')
    ax.set_ylabel(r'$J(\theta)$')
    axs.append(ax)
fig.subplots_adjust(wspace=0.25)

fig.savefig('lrfig7.eps')
