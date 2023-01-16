# 6.10. Composition

'''
As we have already seen, you can call one function from within another. 
This ability to build functions by using other functions is called composition.

As an example, we’ll write a function that takes two points, 
the center of the circle and a point on the perimeter, and computes the area of the circle.
'''


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**.5
    return result

def area(radius):
    b = 3.14159 * radius**2
    return b

def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

print(area2(0, 0, 1, 1))

'''
Note that we could have written the composition without storing the intermediate results.
-----------------------------------------
def area2(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))
-----------------------------------------
'''
