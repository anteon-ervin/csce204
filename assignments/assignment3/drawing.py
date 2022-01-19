# Graphics 
# Author: Anteon Ervin

import turtle 

turtle.bgcolor()

pen = turtle.Turtle()

pen.pensize(10)
pen.speed(.5)
turtle.setup(1000,1000)

# front wheel
pen.up()
pen.setpos(210,-160)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.circle(75)
pen.end_fill()

# back wheel
pen.up()
pen.setpos(-75,-160)
pen.down()
pen.fillcolor("red")
pen.begin_fill()
pen.circle(75)
pen.end_fill()

# bike body
pen.up()
pen.setpos(-75,-100)
pen.down()
pen.forward(150)
pen.left(120)
pen.forward(150)
pen.left(120)
pen.forward(150)

pen.up()
pen.setpos(75,-100)
pen.down()
pen.forward(-150)
pen.left(120)
pen.forward(-150)
pen.left(120)
pen.forward(-150)

# seat
pen.up()
pen.setpos(-4,34)
pen.down()
pen.forward(75)

pen.left(60)
pen.forward(25)
pen.left(180)
pen.forward(50)


# steering
pen.up()
pen.setpos(90,105)
pen.down()
pen.forward(25)
pen.right(60)
pen.forward(230)

turtle.done()



