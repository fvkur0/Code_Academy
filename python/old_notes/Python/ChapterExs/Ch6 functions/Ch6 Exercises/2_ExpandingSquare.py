#2 Draws a repeating, expanding square with each run

import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.fd(sz)
        t.lt(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')
    turt = turtle.Turtle()
    turt.pensize(3)
    sz = 20
    x = -10
    y = -10
    for i in range(25):
        drawSquare(turt, sz)
        turt.penup()
        turt.goto(x,y)
        sz = sz + 20
        x = x - 10
        y = y - 10
        turt.pendown()
        
    wn.exitonclick()

main()

