# Star 
# Author: Anteon Ervin

import turtle 
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.hideturtle()



colors = ("violet", "indigo", "blue", "green","yellow", "orange","red")

for i in range(100):
    starWidth = random.randint(20,80)
    pen.color(colors[i%len(colors)])
    pen.fillcolor(colors[i%len(colors)])
    x = random.randint(-int(turtle.window_width()/2),int(turtle.window_height()/2))
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_width()/2))
    pen.up()
    pen.setpos(x,y)
    pen.down()

    # draw up triangle
    pen.begin_fill()
    for j in range (3):
        pen.forward(starWidth)
        pen.left(120)

    pen.up()
    pen.setpos(0,starWidth/2)
    pen.down()
    pen.end_fill()

    pen.up()
    pen.setpos(x,y+ starWidth/2)
    pen.down()
    # draw up down triangle
    pen.begin_fill()
    for j in range (3):
        pen.forward(starWidth)
        pen.left(-120)
    pen.end_fill()

    
turtle.done()
