"""
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  #print(location)
  for i in location:
    scoops_sold += i

print(scoops_sold)

"""
""""

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [sg + 10 for sg in grades]
print(scaled_grades)

"""
"""

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []

for value in heights:
  if value >= 162:
    can_ride_coaster.append(value)

print(can_ride_coaster)

"""
#"""
#--------review

single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
cubes = []

for digits in single_digits:
  squares.append(digits ** 2)
  #print(digits)

for digits in single_digits:
  cubes.append(digits ** 3)

print(cubes)


