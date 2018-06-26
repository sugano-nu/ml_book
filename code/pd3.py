import pandas as pd
import numpy as np

df = pd.read_csv('../data/ex1data1_test.txt', names=['population','profit'])
m, n = df.shape

df['all_1'] = 1
df['ndarray'] = np.arange(m)
df['list'] = range(m)

print('df=\n{}'.format(df))
