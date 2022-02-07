# Hexagon
# Author: Anteon Ervin

import turtle 

turtle.bgcolor("black")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("red")
pen.fillcolor("teal")

hexagonSize = 50



# draw hexagon 1 
pen.up()
pen.setpos(-hexagonSize*4,hexagonSize)
pen.down()
pen.begin_fill()

for i in range(8):
     pen.forward(hexagonSize)
     pen.left(45)
pen.end_fill()

# draw hexagon 2 
pen.up()
pen.setpos(-hexagonSize*2.3,-hexagonSize*3/4)
pen.down()
pen.begin_fill()

for i in range(8):
     pen.forward(hexagonSize)
     pen.left(45)
pen.end_fill()

# draw hexagon 3 
pen.up()
pen.setpos(-hexagonSize/2.5,-hexagonSize*2.5)
pen.down()
pen.begin_fill()

for i in range(8):
     pen.forward(hexagonSize)
     pen.left(45)    
pen.end_fill()
 
# draw hexagon 4 
pen.up()
pen.setpos(hexagonSize*1.3,-hexagonSize*4.2)
pen.down()
pen.begin_fill()

for i in range(8):
     pen.forward(hexagonSize)
     pen.left(45)    
pen.end_fill()

# draw hexagon 5 
pen.up()
pen.setpos(hexagonSize*3,-hexagonSize*6)
pen.down()
pen.begin_fill()

for i in range(8):
     pen.forward(hexagonSize)
     pen.left(45)
pen.end_fill()

  
     
         
turtle.done()
