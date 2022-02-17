# Graphical List 2
# Author: Anteon Ervin

import turtle 


turtle.setup(600,600)
pen = turtle.Turtle()
turtle.bgcolor("skyblue")
pen.pensize(2)
pen.speed(0)
pen.hideturtle()

colors = []
count = 1
gridSize = int(turtle.numinput("Block","Enter number of rows",5,1,10))
for i in range(gridSize):
    rowColor = (turtle.textinput("Block", f"Enter color of row {count}:")).strip().lower()
    colors.append(rowColor)
    count +=1
    
areaPadding = turtle.window_width()/gridSize/1.1 
square = areaPadding * 1
padding = areaPadding * .1
 

for row in range(gridSize):  
    
    
    x = -turtle.window_width()/2 + areaPadding/6
    y = -turtle.window_height()/2.2 + areaPadding * row + padding
    pen.fillcolor(colors[row%len(colors)]) 
    for col in range(gridSize):
        
        pen.begin_fill()
        pen.up()
        pen.setpos(x,y)
        pen.down()
        
        for i in range(4):
            pen.forward(square)
            pen.left(90)
        pen.end_fill()
        x += areaPadding


        
        

        
turtle.done()
