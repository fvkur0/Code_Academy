def square(x):
    '''raise x to the second power'''
    y = x * x
    return y

import test
print('testing square function')
test.testEqual(square(10), 100)

amt = 10
print(square(amt))

def plusone(b):
    z = b+1
    return z

print('Testing')
test.testEqual(plusone(6), 7)

digit = 5
print(plusone(digit))

