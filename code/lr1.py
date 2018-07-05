import pandas as pd
import numpy as np

df = pd.read_csv('../data/ex1data1.txt', names=['population','profit'])

df['all_1'] = 1
X = df[['all_1','population']].values
y = df['profit'].values
y = np.c_[y]

print('X=\n{}\n......\ntype={},shape={}'.format(X[:5],type(X),X.shape))
print('y=\n{}\n......\ntype={},shape={}'.format(y[:5],type(y),y.shape))
