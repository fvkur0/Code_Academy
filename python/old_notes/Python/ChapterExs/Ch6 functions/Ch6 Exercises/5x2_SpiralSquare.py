import turtle

x = 300
ang = 111
travle = 5

def spiralSquare(t, dis):
        t.rt(ang)
        t.fd(dis)

def main():
    wn = turtle.Screen()
    wn.bgcolor('black')
    burt = turtle.Turtle()
    burt.color('lightgreen')
    burt.pensize(4)
    burt.speed(10)
    travle = 3
    for i in range(x):
        spiralSquare(burt, travle)
        travle = travle + 3
    wn.exitonclick()

main()

