# Python Code Challenges, Control Flow

#"""
# 1. Large Power

print("Is the product greater than 5000? ")

base = int(input("What is your number? "))
exponent = int(input("What is your exponent? "))
product = base ** exponent

def power(base, exponent):
    if base ** exponent <= 5000:
        return False
    else:
        return True

if power(base, exponent) == True:
    print("Yup, its over 5000 at " + str(product))
else:
    print("Its under 5000 at " + str(product))

#"""
#---------------------------------------------------------------------------------
"""
# 2. Over Budget

def calc(budget, food_bill, electricity_bill, internet_bill, rent):    
    if (budget < food_bill + electricity_bill + internet_bill + rent):
        return False
    else:
        return True
        
budget = int(input("What is your budget? "))
food_bill = int(input("How much do you need for food? "))
electricity_bill = int(input("How much are you paying for power? "))
internet_bill = int(input("How much are you paying for internet? "))
rent = int(input("How much is your rent? "))

if calc(budget, food_bill, electricity_bill, internet_bill, rent) == True:
    print("You're under budget")
else:
    print("You're over budget")

#"""
#---------------------------------------------------------------------------------
"""
# 3. Twice as Large

def doubler(num1, num2):
    if (num1 > num2 * 2):
        return True
    else:
        return False

print(doubler(10, 5))
print(doubler(11, 5))

#"""
#---------------------------------------------------------------------------------
"""
# 4. Divisible by 10

def dby10(num):
    if num % 10 == 0:
        return True
    else:
        return False

print(dby10(20))
print(dby10(25))

#"""
#---------------------------------------------------------------------------------
"""
# 5. Not Sum To Ten

def ns2t(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False

print(ns2t(9, -1))
print(ns2t(9, 1))
print(ns2t(5, 5))

#"""
#---------------------------------------------------------------------------------