import turtle 


polygon = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("green")

num_sides = int(input("sides? "))
side_length = int(input("Length"))
angle = 360.0 / num_sides 

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()
