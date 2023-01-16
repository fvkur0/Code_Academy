
import turtle

def drawRectangle(t, w, h):
    for i in range(2):
        t.fd(w)
        t.lt(90)
        t.fd(h)
        t.lt(90)

def drawSquare(tx, sz):
    drawRectangle(tx, sz, sz)

wn = turtle.Screen()
wn.bgcolor("green")
tess = turtle.Turtle()
drawSquare(tess, 100)
wn.exitonclick()