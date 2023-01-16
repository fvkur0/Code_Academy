def square(x):
    '''raise x to the second power'''
    return x * x

import test
print('testing square function')
test.testEqual(square(10), 100)

#--First demonstration of the test module

def half(y):
    return y/2

print('testing...')
test.testEqual(half(6), 3)

def double(z):
    return z*2

print('testing...')
test.testEqual(double(6), 12)