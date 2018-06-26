import pandas as pd
import numpy as np

df = pd.read_csv('../data/ex1data1_test.txt', names=['population','profit'])
m, n = df.shape

df['all_1'] = 1
df['ndarray'] = np.arange(m)
df['list'] = range(m)

df_sub1 = df['profit']
df_sub2 = df[['list','population']]

df_sub3 = df[0:1]
df_sub4 = df[2:4]

df_sub5 = df.loc[3:6,'list']
df_sub6 = df.loc[::2,['profit','ndarray']]

print('df_sub1=\n{}\ntype={}\n'.format(df_sub1,type(df_sub1)))
print('df_sub2=\n{}\ntype={}\n'.format(df_sub2,type(df_sub2)))
print('df_sub3=\n{}\ntype={}\n'.format(df_sub3,type(df_sub3)))
print('df_sub4=\n{}\ntype={}\n'.format(df_sub4,type(df_sub4)))
print('df_sub5=\n{}\ntype={}\n'.format(df_sub5,type(df_sub5)))
print('df_sub6=\n{}\ntype={}\n'.format(df_sub6,type(df_sub6)))
