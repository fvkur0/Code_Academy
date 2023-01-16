import turtle

x = 132

def spiralSquare(t, dis):
        t.rt(90)
        t.fd(dis)
        dis = dis + 3

def main():
    wn = turtle.Screen()
    wn.bgcolor('green')
    burt = turtle.Turtle()
    burt.color('blue')
    burt.pensize(3)
    burt.speed(10)
    for i in range(x):
        spiralSquare(burt, 3)
    wn.exitonclick()

main()

