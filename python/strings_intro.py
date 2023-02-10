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

"""

def get_length(string):
    count = 0
    for letters in string:
        count += 1
        #print(count)
    print(count)

get_length("corruption")

#"""

"""

def letter_check(word, letter):
    for i in word:
        if i == letter:
            return True
        else:
            return False

print(letter_check('abracadabra', 'a'))
print(letter_check('abracadabra', 'z'))

#"""

"""

def contains(big_string, little_string):
    return little_string in big_string
       
def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common

print(common_letters("welcome to the jungle", "An apple a day"))

#"""

#"""
#REVIEW

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        username = first_name
    else:
        username = first_name[:3]
    if len(last_name) < 4:
        username += last_name
    else:
        username += last_name[:4]
    
    return username

print(username_generator('Patrick', 'Myers'))

def password_generator(username):
    password = ''
    for i in range(0, len(username)):
        password += username[i-1]
    return password

print(password_generator(username_generator('Wolfgang', 'Marin')))

#"""