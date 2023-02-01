"""

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[5:]

"""

"""
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
    length1 = len(first_name)
    length2 = len(last_name)
    firs3 = first_name[length1-3:]
    las3 = last_name[length2-3:]
    print(firs3 + las3)

password_generator("Reiko", "Matsuki")

# ""  CA Solution:
def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)

"""

"""

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

#"""

#"""



#"""