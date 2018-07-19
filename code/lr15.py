import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('../data/ex1data2.txt', names=['area','bedroom','price'])
X = df[['area','bedroom']].values
y = df['price'].values
y = np.c_[y]

lr2 = LinearRegression()
lr2.fit(X, y)

X_pred = np.array([[2500,3]])
y_pred = lr2.predict(X_pred)

print('y_pred={}'.format(y_pred[0,0]))
