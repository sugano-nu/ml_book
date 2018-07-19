import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MyLinearRegression:

    def __init__(self, alpha=0.01, itera=1500):
        self.alpha= alpha
        self.itera = itera

    def fit(self, X, y, init_theta=None):

        def add1(X):
            m,n = X.shape
            all1 = np.ones(m)
            return np.c_[all1, X]

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

        X = add1(X)
        if init_theta is None:
            m,n = X.shape
            init_theta = np.zeros(n)
            init_theta = np.c_[init_theta]
        self.theta, self.theta_hist, self.J_hist = \
            gradient_descent(X, y, init_theta, self.alpha, self.itera)

    def predict(self, X):

        def add1(X):
            m,n = X.shape
            all1 = np.ones(m)
            return np.c_[all1, X]

        def hypo_function(X, theta):
            y_pred = X.dot(theta)
            return y_pred

        X = add1(X)
        self.y_pred = hypo_function(X, self.theta)
        return self.y_pred

df = pd.read_csv('../data/ex1data2.txt', names=['area','bedroom','price'])
X = df[['area','bedroom']].values
y = df['price'].values
y = np.c_[y]

lr = MyLinearRegression(alpha=0.00000003,itera=50)
lr.fit(X, y)
X_pred = np.array([[2500,3]])
y_pred = lr.predict(X_pred)

print('y_pred={}'.format(y_pred[0,0]))

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
m = len(lr.J_hist)
ax.plot(np.arange(m), lr.J_hist)
ax.set_xlabel('iter')
ax.set_ylabel(r'$J(\theta)$')

fig.savefig('lrfig11.eps')
