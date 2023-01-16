
def square(x):
    y = x * x
    return y

def sum_of_squares(x, y, z):
    a = square(x)
    b = square(y)
    c = square(z)
    return a + b + c

a = -5 #25
b = 2 #4
c = 10 #100
result = sum_of_squares(a, b, c)
print(result)
#---Result is 129
#-----------------------------------------