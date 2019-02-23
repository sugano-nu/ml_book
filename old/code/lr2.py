import pandas as pd
import numpy as np

def hypo_function(X, theta):
    y_pred = X.dot(theta)
    return y_pred

df = pd.read_csv('../data/ex1data1.txt', names=['population','profit'])

df['all_1'] = 1
X = df[['all_1','population']].values
y = df['profit'].values
y = np.c_[y]

THETA = np.array([[1],[-2]])

y_pred = hypo_function(X, THETA)

y_matrix = np.c_[y, y_pred]
y_df = pd.DataFrame(y_matrix, columns=['y','y_pred'])

print('y_df=\n{}'.format(y_df.head(5)))
