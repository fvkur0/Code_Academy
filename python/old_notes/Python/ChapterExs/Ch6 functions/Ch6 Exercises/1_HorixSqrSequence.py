# Chapter 6.13 Exercises
# 1 Draws 5 squares next to eachother

import turtle

def drawSquare(t, sz):
    for i in range(5):
        for i in range(4):
            t.fd(sz)
            t.lt(90)
        t.penup()    
        t.fd(sz*2)
        t.pendown()

def main():
    wn = turtle.Screen()
    #wn.setworldcoordinates(50, 50, 50, 50)
    wn.bgcolor('lightgreen')
    turt = turtle.Turtle()
    turt.color('pink')
    turt.pensize(3)
    drawSquare(turt, 20)
    wn.exitonclick()

main()
