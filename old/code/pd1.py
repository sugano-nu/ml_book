import pandas as pd

df = pd.read_csv('../data/ex1data1.txt', names=['population','profit'])
m, n = df.shape
print('df=\n{}\ntype={}\nlow_num={}, col_num={}'.format(df.head(10), type(df), m, n))
