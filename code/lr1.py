import pandas as pd
import numpy as np

df = pd.read_csv('../data/ex1data1_test.txt', names=['population','profit'])

df['all_1'] = 1
X = df[['all_1','population']].values
y = df['profit'].values
y = np.c_[y]

print('X=\n{}\ntype={},shape={}'.format(X,type(X),X.shape))
print('y=\n{}\ntype={},shape={}'.format(y,type(y),y.shape))
