# Control Flow Advance

"""
# 1. In Range

def inrange(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False 

print(inrange(10, 10, 10)) 
print(inrange(5, 10, 20)) 

#"""

""" 
# 2. Same Name 
 
def samename(your_name, my_name):
    if your_name == my_name:
        return True
    else:
        return False

print(samename("colby", "colby"))
print(samename("tina", "amber"))

#"""

"""
# 3. Always False

def always_false(num):
    if num > num and num < num:
        return True
    else:
        return False

print(always_false(0))
print(always_false(-1))
print(always_false(1))

#"""

"""
# 4. Movie Review

def review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating > 5 and rating < 9:
        return "This one was fun."
    else:
        return "Outstanding!"

print(review(9))
print(review(4))
print(review(6))

#"""

#"""
# 5. Max Number

def maxnum(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "Its a tie!"

print(maxnum(-10, 0, 10))
print(maxnum(-10, 5, -30))
print(maxnum(-5, -10, -10))
print(maxnum(2, 3, 3))

#"""