import pandas as pd

df = pd.read_csv('../data/ex1data1_test.txt', names=['population','profit'])

pop = df['population'].values
print('population={},type={}'.format(pop,type(pop)))
