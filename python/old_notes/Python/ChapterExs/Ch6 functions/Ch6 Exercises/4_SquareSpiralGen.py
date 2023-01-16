import turtle

rot = int(input('How many turns? '))
# 11 for Oderus

def drawSquare(t, sz):
    for i in range(4):
        t.fd(sz)
        t.lt(90)
    t.lt(360/rot)

def main():
    wn = turtle.Screen()
    wn.bgcolor('black')
    turt = turtle.Turtle()
    turt.color('lightgreen')
    turt.speed(10)
    turt.pensize(2)
    for i in range(rot):
        drawSquare(turt, 200)

    wn.exitonclick()

main()