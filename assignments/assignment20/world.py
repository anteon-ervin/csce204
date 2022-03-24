# World
# Author: Anteon Ervin
import turtle

turtle.bgcolor("skyblue")
turtle.setup(1100, 300)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()



def getScene():
    sceneItems = []
    with open('assignments/assignment20/scene.txt') as file:
        for line in file: 
            sceneItem = line.replace("\n","").strip().lower()
            sceneItems.append(sceneItem)
        return sceneItems
    
def drawFlower(x,y,size):
    #stem
    pen.up()
    pen.setheading(270)
    pen.setposition(x,y)
    pen.down()
    pen.pencolor("green")
    pen.forward(50) 
    
    #pedals
    pen.up()
    pen.setheading(0)
    pen.setposition(x,y)
    pen.down()
    pen.pencolor("red")
    for i in range (30):
        pen.circle(50,60)
        if i % 2 ==0:
            pen.circle(0,100)
    pen.setheading(0)
   
def drawTree(x,y,size):
    trunkHeight = size/2
    
    #trunk
    pen.up()
    pen.setheading(270)
    pen.setposition(x,y)
    pen.down()
    pen.pencolor("saddle brown")
    pen.fillcolor("brown")
    pen.pensize(20)
    pen.forward(50)
    pen.pensize(2)

    #leaves
    pen.up()
    pen.setheading(0)
    pen.setposition(x,y)
    pen.down()
    pen.pencolor("green")
    pen.fillcolor("green")
    pen.begin_fill()
    pen.circle(size/4)
    pen.end_fill()
    
size = 120    
items = getScene()
padding = size
x = -turtle.window_width()/2+padding
y = turtle.window_height()/2 - padding


for item in items:
    if item == "tree":
        drawTree(x, y, size)
        x += padding
        
    elif item == "flower":
        drawFlower(x, y, size)
        x += padding

    

turtle.done()

    
    