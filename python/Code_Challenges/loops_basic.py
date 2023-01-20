"""
# 1. Divisible By Ten

def divisible_by_ten(nums):
    count = 0
    for i in nums:
        if i % 10 == 0:
            count += 1
    return count
print(divisible_by_ten([20, 25, 30, 35, 40]))

#"""

"""
# 2. Greetings

def add_greetings(names):
    lst = []
    for name in names:
        lst.append("Hello, " + name)
    return lst

print(add_greetings(["Owen", "Max", "Sophie"]))

#"""

"""
# 3. Delete Starting Even Numbers

def delete_starting_evens(lst):
   while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
    return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))

#"""

"""
# 4. Odd Indices

def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))

#"""

#"""
# 5. Exponents

def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))

#"""