n=input("Please enter your name: " )
print("hello", n)

#--- Input function returns a string value.
#--- Dont Forget to convert the string into an int or float
#-- == is equal to
#-- != is not equal to

str_seconds = input("Please enter the number of seconds you wish to convert: ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)

#---------------------------------------------------------------------------------------------------
#--- Exercise 1

print("Many people keep time using a 24 \
 hour clock (11 is 11am and 23 is 11pm, 0 is midnight). \
 If it is currently 13 and you set your alarm to go off in 50 hours, \
 it will be 15 (3pm). Write a Python program to solve the general version of the above problem. \
 Ask the user for the time now (in hours), and then ask for the number of hours to wait for the alarm. \
 Your program should output what the time will be on the clock when the alarm goes off.")

ch_str = input("What is the current hour in military time?: ")
ch_mthours = int(ch_str)
cm_str = input("How many minutes in the current hour?: ")
cm_mthours = int(cm_str)

ht_str = input("How many hours till alarm?: ")
ht = int(ht_str)
mt_str = input("How many minutes till alarm?: ")
mt = int(mt_str)

hours = (ht % 24)
minutes = (mt % 60)

final_hours = (ch_mthours + hours)
final_minutes = (cm_mthours + minutes)

if final_hours >= 24:
    final_hours = (final_hours - 24)

if final_minutes > 60:
    final_hours = (final_hours + 1)
    final_minutes = (final_minutes - 60)
    

if final_hours == 0: #--reference top for not equal to
    print("The time will be", final_minutes, "minutes past midnight")
else:
    ("The hour will be", final_hours, "with", final_minutes, "left in the hour")

input("Press 'enter' to exit ;")

#------------------------------------------------------------------------------------------------------------