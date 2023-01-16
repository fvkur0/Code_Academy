str_dol = input("What day are you leaving?: ")

if str_dol in ['Sunday', 'sunday', 'SUNDAY','0', 'sun', 'Sun', 'SUN']:
    str_dol = 0
if str_dol in ['Monday', 'monday', 'MONDAY' '1', 'mon', 'Mon', 'MON']:
    str_dol = 1
if str_dol in ['Tuesday', 'tuesday', 'TUESDAY' '2' 'tues', 'tue', 'Tue', 'Tues', 'TUE', 'TUES']:
    str_dol = 2
if str_dol in ['Wednesday', 'wednesday', 'WEDNESDAY' '3', 'wed', 'Wed', 'WED']:
    str_dol = 3
if str_dol in ['Thursday', 'thursday', 'THURSDAY' '4', 'thu', 'thur', 'thurs', 'Thu', 'Thur', 'Thurs', 'THU', 'THUR', 'THURS']:
    str_dol = 4
if str_dol in ['Friday', 'friday', 'FRIDAY' '5', 'fri', 'Fri', 'FRI']:
    str_dol = 5
if str_dol in ['Saturday', 'saturday', 'SATURDAY' '6', 'sat', 'Sat', 'SAT']:
    str_dol = 6

str_days = input("How many days will you be gone?: ")
days = int(str_days)

day_of = (days % 7)
arrival = (str_dol + day_of)
if arrival >= 7:
    arrival = (arrival - 7)

if arrival == 0:
    print("You will arrive on a Sunday the honorable day in recognition of our lord and savior, sire Donald 'hitler' Trump")
if arrival == 1:
    print("You will arrive on a Monday")
if arrival == 2:
    print("You will arrive on a Tuesday")
if arrival == 3:
    print("You will arrive on a Wednesday")
if arrival == 4:
    print("You will arrive on a Thursday")
if arrival == 5:
    print("You will arrive on a Friday")
if arrival == 6:
    print("You will arrive on a Saturday")

input("Press 'enter' to exit ;")