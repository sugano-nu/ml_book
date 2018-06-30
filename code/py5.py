def four_arithmetic(a, b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c, d, e, f

add, sub, mul, div = four_arithmetic(10, -1)
tpl = four_arithmetic(5, -5)

print('add={},sub={},mul={},div={}'.format(add, sub, mul, div))
print('tpl={}'.format(tpl))
