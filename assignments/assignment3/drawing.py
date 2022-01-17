# Graphics 
# Author: Anteon Ervin

import turtle 

turtle.bgcolor("skyblue")

pen = turtle.Turtle()

pen.pensize(10)
pen.speed(.5)
turtle.setup(1000,1000)
# snowman head
pen.up()
pen.setpos(0,100)
pen.down()
pen.color("white")
pen.fillcolor("white")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# snowman eyes
pen.up()
pen.setpos(20,150)
pen.down()
pen.color("black")
pen.circle(5)

pen.up()
pen.setpos(-20,150)
pen.down()
pen.circle(5)

# snowman nose
pen.up()
pen.setpos(0,135)
pen.down()
pen.color("orange")
pen.forward(5)
pen.left(2)
pen.forward(5)
pen.left(2)
pen.forward(5)

# snowman mouth
pen.up()
pen.setpos(0,120)
pen.down()
pen.color("saddle brown")
pen.circle(.1)

pen.up()
pen.setpos(-10,122)
pen.down()
pen.circle(.1)

pen.up()
pen.setpos(-15,125)
pen.down()
pen.circle(.1)

pen.up()
pen.setpos(10,122)
pen.down()
pen.circle(.1)


# snowman stomach
pen.up()
pen.setpos(0,-100)
pen.down()
pen.color("white")
pen.fillcolor("white")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# snowman buttons 
pen.up()
pen.setpos(0,30)
pen.down()
pen.color("red")
pen.circle(5)

pen.up()
pen.setpos(0,70)
pen.down()
pen.circle(5)

pen.up()
pen.setpos(0,-10)
pen.down()
pen.circle(5)

pen.up()
pen.setpos(0,-50)
pen.down()
pen.circle(5)

pen.up()
pen.setpos(0,-90)
pen.down()
pen.circle(5)

# snowman arms
pen.up()
pen.setpos(100,-10)
pen.down()
pen.color("saddle brown")
pen.forward(100)

pen.up()
pen.setpos(-210,-10)
pen.down()
pen.forward(100)
    
# snowman legs
pen.up()
pen.setpos(0,-400)
pen.down()
pen.color("white")
pen.fillcolor("white")
pen.begin_fill()
pen.circle(150)
pen.end_fill()

#snow
pen.up()
pen.setpos(200,200)
pen.down()
pen.color("white")
pen.circle(2)

pen.up()
pen.setpos(150,100)
pen.down()
pen.color("white")
pen.circle(2)

pen.up()
pen.setpos(-220,200)
pen.down()
pen.color("white")
pen.circle(2)

pen.up()
pen.setpos(-150,100)
pen.down()
pen.color("white")
pen.circle(2)

pen.up()
pen.setpos(0,250)
pen.down()
pen.color("white")
pen.circle(2)

turtle.done()

