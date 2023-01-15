print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
#weight = 185
#planet = 3

# Write an if statement below:

visitor = input('...Who are you? ')
print('Welcome, ' + visitor + '.')

planet = int(input('Please select a planet from the index above to find out what you weigh there. '))

weight = float(input('How much do you weigh right now? '))

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19


print(('You weigh ') + str(weight))

