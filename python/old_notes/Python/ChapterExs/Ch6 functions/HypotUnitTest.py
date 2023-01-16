#Unit test on hypotenuse 

import test
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**.5
    return result

'''
Try changing the expected result of the test
The module will return actual expected value in the event of a failure
'''

test.testEqual(distance(1, 2, 1, 2), 0)
test.testEqual(distance(1, 2, 4, 6), 5)
test.testEqual(distance(0, 0, 1, 1), 1.41421)
test.testEqual(distance(0, 0, 1, 1), 1.41) #This will fail the test
test.testEqual(distance(0, 0, 1, 1), 1.41, 2) #(1.41, 2) is the range of acceptable return


