import pandas as pd

df = pd.read_csv('../data/ex1data1_test.txt', names=['population','profit'])

array_1 = df.values
array_2 = df['population'].values
array_3 = df[0:1].values
array_4 = pd.DataFrame(df['profit']).values

print('array_1=\n{}\ntype={}\nshape={}\n'.format(array_1,type(array_1),array_1.shape))
print('array_2=\n{}\ntype={}\nshape={}\n'.format(array_2,type(array_2),array_2.shape))
print('array_3=\n{}\ntype={}\nshape={}\n'.format(array_3,type(array_3),array_3.shape))
print('array_4=\n{}\ntype={}\nshape={}'.format(array_4,type(array_4),array_4.shape))
