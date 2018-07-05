import pandas as pd
import numpy as np

def gradient_descent(X, y, theta, alpha, itera):
    m, n = X.shape
    for i in range(itera):
        J_grad = 1 / m * (X.T.dot(X).dot(theta) - X.T.dot(y))
        theta = theta - alpha * J_grad
    return theta

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
THETA = np.array([[1],[-2]])

theta = gradient_descent(X, y, THETA, ALPHA, ITERA)
print('1: theta=\n{}'.format(theta))

J = cost_function(X, y, theta)
print('2: J={}'.format(J))

X_pred = np.array([[1, 7.532]])
y_pred = hypo_function(X_pred, theta)
y_pred = y_pred[0,0]
print('3: y_pred={}'.format(y_pred))
