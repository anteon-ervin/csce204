# Midterm
# Author: Anteon Ervin

import turtle 
import random

turtle.setup(575,575)
pen = turtle.Turtle()
turtle.bgcolor("black")
pen.pensize(2)
pen.speed(0)
pen.hideturtle()

names = []
colors = []

counter = 0
number = int(turtle.numinput("Stars","Enter number of stars: ",5,1,10))

for i in range(number):
    counter += 1 
    name = (turtle.textinput("Star Name", f"Enter Star {counter} name:"))
    names.append(name)
        
    color = (turtle.textinput(F"Star Color", f"Enter Star {counter} color:"))
    colors.append(color)
 

areaPadding = turtle.window_width()/number 
starWidth = 140 / number
padding = areaPadding * 1.5
turtle.color("white")
style = ("Arial",50, "bold")
# Title   
turtle.up()
turtle.setpos(-turtle.window_width(),turtle.window_height()/2)
turtle.down()
turtle.write("Beautiful Stars", font = style)

# Moon
turtle.up()
turtle.goto(turtle.window_width()/1,turtle.window_height()/2.5)
turtle.color('white')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

turtle.color('black')
turtle.begin_fill()
turtle.forward(50)
turtle.circle(100)
turtle.end_fill()



for i in range(1):
    
    turtle.up()
    
    
    x = -turtle.window_width()/2 + starWidth *3 
    turtle.down()
    
    for col in range(number):
        
        y = random.randint(-400,90)
        
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color(colors[col%len(colors)])
        pen.fillcolor(colors[col%len(colors)])
        # triangle
        pen.begin_fill()
        for j in range (3):
            pen.forward(starWidth)
            pen.left(120)

        pen.up()
        pen.setpos(x,starWidth/2)
        pen.down()
        pen.end_fill()

        pen.up()
        pen.setpos(x,y+ starWidth/2)
        pen.down()
        # triangle
        pen.begin_fill()
        for j in range (3):
            pen.forward(starWidth)
            pen.left(-120)
        pen.end_fill()
        pen.up()
        pen.setpos(x,y+starWidth)
        pen.down
        pen.color("white")
        style2 = ("Arial",int(starWidth/2), "bold")
        pen.write(names[col%len(names)], font = style2)
        x += padding
 

# Rocket    
pen.up()
pen.setpos(0,300)
pen.down()
for i in range(4):
    pen.fillcolor("red")
    pen.color("red")
    pen.begin_fill()
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.end_fill()

pen.fillcolor("yellow")    
pen.up()
pen.setpos(100,300)
pen.down()
pen.begin_fill()
pen.setheading(45)
pen.forward(50)
pen.setheading(155)
pen.forward(40)
pen.end_fill()
    

turtle.done()
