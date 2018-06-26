import pandas as pd

df = pd.read_csv('../data/ex1data1_test.txt', names=['population','profit'])
m, n = df.shape
print('df=\n{}\ntype={}\nlow_num={}, col_num={}'.format(df, type(df), m, n))
