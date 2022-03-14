# Click Picture
# Author: Anteon Ervin

import turtle
import random
turtle.setup(800,500)
turtle.bgcolor("lightgrey")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()


colors = ("violet", "indigo", "blue", "green","yellow", "orange","red")


def draw_car(x,y):
    draw_body(x, y)
    draw_tire(x-carWidth/4.5, y-carWidth/4)
    draw_tire(x+carWidth/4.5, y-carWidth/1.7)

carWidth = 100
def draw_body(x,y):
    
        color = random.choice(colors)
        pen.up()
        pen.setpos(x-carWidth/2,y-carWidth/4)
        pen.down()
        pen.color(color)
        pen.fillcolor(color)
        pen.begin_fill()
        pen.forward(carWidth)
        pen.left(90)
        pen.forward(carWidth/3)
        pen.left(90)
        pen.forward(carWidth)
        pen.end_fill()

tireRadius = carWidth/6
def draw_tire(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor("black")
    pen.begin_fill()
    pen.circle(tireRadius)
    pen.end_fill()
    pen.setheading(0)
    

lineLength = 90
x = -turtle.window_width()/2
for i in range(8):
    pen.color("yellow")
    pen.up()
    pen.setpos(x,0)
    pen.down()
    pen.forward(lineLength)
    x += 100
    
turtle.onscreenclick(draw_car)
turtle.done()


