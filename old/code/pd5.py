import pandas as pd
import numpy as np

df = pd.read_csv('../data/ex1data1_test.txt', names=['population','profit'])

df_sub1 = df['profit']
df_sub2 = df[2:3]

print('df_sub1=\n{}\ntype={}\nshape={}\n'.format(df_sub1,type(df_sub1),df_sub1.shape))
print('df_sub2=\n{}\ntype={}\nshape={}\n'.format(df_sub2,type(df_sub2),df_sub2.shape))

df_sub3 = pd.DataFrame(df_sub1)

print('df_sub3=\n{}\ntype={}\nshape={}\n'.format(df_sub3,type(df_sub3),df_sub3.shape))
