'''Refined PolyGen from lab'''

import turtle

def drawPoly(t, sideLength, numSides):
    for i in range(numSides):
        t.fd(sideLength)
        t.lt(360/numSides)

wn = turtle.Screen()
wn.bgcolor("green")
jen = turtle.Turtle()

drawPoly(jen, 50, 15)

wn.exitonclick()