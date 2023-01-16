"""

print("Checking the weather for you!")

def weather_check():
  print("Looks great outside! Enjoy your trip.")
  print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()

"""
"""

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")

"""

"""

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    print(car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses(200, 100, 100, 5)

"""

"""

def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
trip_planner("Brooklyn", "Queens")

"""

"""

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:

max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)
rounded_price = round(tshirt_price, 1)
print(rounded_price)

"""

