# Graphical Functions 
# Author: Anteon Ervin

import turtle 
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(0)
pen.hideturtle()

colors = ("violet", "indigo", "blue", "green","yellow", "orange","red")

def draw_triangle(width,color):
    
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        
        
        
        pen.down()
        pen.forward(width)
        pen.left(-120)
    pen.end_fill()
    
def draw_art_cube(x, y, size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    
    width = random.randint(20, 100)
    trianglePadding = width/2 
    angle = 0
    for i in range(6):
        color = random.choice(colors)
        if i % 2 == 0:
            
            pen.up()
            pen.setpos(x,y)
            pen.setheading(angle)
            pen.down()
            draw_triangle(width, f"{color}")
            angle += 60
        if i % 1 == 0:
            
            pen.up()
            pen.setpos(x,y)
            pen.setheading(angle)
            pen.down()
            
            draw_triangle(width, f"{color}")
            angle += 120
                   
cubePadding = 100             

       
    
for i in range(20):
    x = random.randint(-int(turtle.window_width()/2),int(turtle.window_height()/2)-cubePadding*2.5)
    y = random.randint(-int(turtle.window_height()/2),int(turtle.window_width()/2)-cubePadding*3)
    draw_art_cube(x, y, 100)

turtle.done()