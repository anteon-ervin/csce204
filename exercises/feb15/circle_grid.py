# Circle
# Author: Anteon Ervin

import turtle 
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)
pen.hideturtle()

gridSize = int(turtle.numinput("Size","Enter size ",5,1,10))
diamterPadding = turtle.window_width()/gridSize
radius = diamterPadding * .8 /2 
padding = diamterPadding * .1

for row in range(gridSize):
    x = -turtle.window_width()/2 + diamterPadding/2
    y = -turtle.window_height()/2 + diamterPadding * row + padding
    
    for col in range(gridSize):
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.circle(radius)
        x += diamterPadding

        
turtle.done()
