import numpy as np

x = np.array([np.e, np.log(3), 10, np.log10(3)])

print('e^x={}'.format(np.exp(x)))
print('log(x)={}'.format(np.log(x)))
print('10^x={}'.format(10 ** x))
print('log10(x)={}'.format(np.log10(x)))
