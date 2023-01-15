weight = 1.5
drone_weight = (weight)

# ground shipping

if weight <= 2:
  weight = (weight * 1.5)
elif weight <= 6:
  weight = (weight * 3.0)
elif weight <= 10:
  weight = (weight * 4)
elif weight > 10:
  weight = (weight * 4.75)

ground_shipping = 20
premium_ground = 125
weight = (weight + ground_shipping)

print("Ground shipping Premium $", premium_ground)

# drone shipping

if drone_weight <= 2:
    drone_weight = (drone_weight * 4.5)
elif drone_weight <=6:
    drone_weight = (drone_weight * 9)
elif drone_weight <=10:
    drone_weight = (drone_weight * 12)
elif drone_weight > 10:
    drone_weight = (drone_weight * 14.25)



print("Ground shipping standard $", weight)
print("Drone shipping rate $", drone_weight)

