import pandas as pd

df = pd.read_csv('../data/ex1data1_test.txt', names=['population','profit'])
print('df=\n{}\ntype={}'.format(df,type(df)))
