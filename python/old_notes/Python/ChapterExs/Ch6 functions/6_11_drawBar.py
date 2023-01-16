# 6.11. A Turtle Bar Chart

'''
Recall from our discussion of modules that there were a number of things that turtles can do. 
Here are a couple more tricks (remember that they are all described in the module documentation).

We can get a turtle to display text on the canvas at the turtle’s current position. 
The method is called write. For example, alex.write("Hello") would write the string hello at the current position.

One can fill a shape (circle, semicircle, triangle, etc.) with a fill color. 
It is a two-step process. First you call the method begin_fill, for example alex.begin_fill(). 
Then you draw the shape. Finally, you call end_fill ( alex.end_fill()).

We’ve previously set the color of our turtle - we can now also set it’s fill color, 
which need not be the same as the turtle and the pen color. 
To do this, we use a method called fillcolor, for example, alex.fillcolor("red").

Ok, so can we get tess to draw a bar chart? Let us start with some data to be charted,

xs = [48, 117, 200, 240, 160, 260, 220]

Corresponding to each data measurement, we’ll draw a simple rectangle of that height, 
with a fixed width. Here is a simplified version of what we would like to create.

'''




import turtle




def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.penup()
    t.fd(5)
    t.write(str(height))
    t.bk(5)
    t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape



xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()             # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("lightgreen")

tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")

if xs >= [200]:
    tess.fillcolor("red")
else: 
    if xs >= [100]:
        tess.fillcolor("yellow")
    else:
        if xs <= [100]:
            tess.fillcolor("green")

tess.pensize(3)



for a in xs:
    drawBar(tess, a)

wn.exitonclick()