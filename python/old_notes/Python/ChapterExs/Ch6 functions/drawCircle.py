import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.fd(sideLength)
        t.rt(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 60)

wn.exitonclick()
