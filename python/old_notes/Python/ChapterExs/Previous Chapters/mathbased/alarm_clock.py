ch_str = input("What is the current hour in military time?: ") #---16
ch_mthours = int(ch_str)
cm_str = input("How many minutes in the current hour?: ") #---20
cm_mthours = int(cm_str)

ht_str = input("How many hours till alarm?: ") #---24
ht = int(ht_str)
mt_str = input("How many minutes till alarm?: ") #---0
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
    

if final_hours == 0:
    print("The time will be", final_minutes, "minutes past midnight")
else:
    print("The hour will be", final_hours, "with", final_minutes, "minutes left in the hour")

input("press enter to exit ;")
