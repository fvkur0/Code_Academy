import random
import math

prob = random.random()
print(prob)

dicethrow = random.randrange(1,7)
print(dicethrow)

#-----------------------------

result = prob * 5
print(result)

#-----------------------------
#Ch.5 Random module exercises

for i in range(10):
    print(random.randrange(0, 100))

#-----------------------------

side1 = 3
side2 = 4
hypotenuse = math.hypot(side1, side2)
print(hypotenuse)

#-----------------------------

