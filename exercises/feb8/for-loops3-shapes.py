# Shapes
# Author: Anteon Ervin

import turtle 

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")


squareSize = 100

pen.up()
pen.setpos(100,100)
pen.down()

#draw a square
for i in range(4):
    pen.forward(squareSize)
    pen.left(90)
    
pen.up()
pen.setpos(-100,100)
pen.down()
triangleSize = 100

#draw a triangle 
for i in range(3):
    pen.forward(triangleSize)
    pen.left(120)
    
turtle.done()
