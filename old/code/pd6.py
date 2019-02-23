import numpy as np
import pandas as pd

array_2d = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
colnames = ['col1', 'col2', 'col3']

df = pd.DataFrame(array_2d, columns=colnames)
print('df=\n{}'.format(df))
