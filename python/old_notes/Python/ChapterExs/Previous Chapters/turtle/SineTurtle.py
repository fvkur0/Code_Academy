
import turtle
import math

t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-190,-190,190,190)
wn.bgcolor("green")
t.speed(10)

t.penup()
t.fd(180)
t.pendown()
t.stamp()
t.lt(180)
t.fd(360)
t.stamp()
t.bk(9)
t.rt(90)
t.penup()
t.bk(4.5)
t.pendown()

for y in range(1,20):
    t.fd(9)
    t.penup()
    t.rt(90)
    t.fd(9)
    t.rt(90)
    t.pendown()
    t.fd(9)
    t.lt(90)
    t.penup()
    t.fd(9)
    t.lt(90)
    t.pendown()

t.fd(9)
t.bk(4.5)
t.lt(90)
t.fd(171)
t.lt(90)
t.penup()
t.fd(180)
t.pendown()
t.stamp()
t.lt(180)
t.fd(360)
t.stamp()
t.bk(18)
t.rt(90)
t.bk(9)

for y in range(1,10):
    t.fd(18)
    t.penup()
    t.rt(90)
    t.fd(18)
    t.rt(90)
    t.pendown()
    t.fd(18)
    t.lt(90)
    t.penup()
    t.fd(18)
    t.lt(90)
    t.pendown()

t.fd(18)
t.penup()
t.goto(-180,0)
t.pendown()


for i in range(-180,181):
    t.goto(i, math.sin(math.radians(i)) * 100)

wn.exitonclick()
