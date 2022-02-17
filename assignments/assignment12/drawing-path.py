# Graphical List
# Author: Anteon Ervin

import turtle


turtle.setup(575,575)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.hideturtle()

xS = []
yS = []

counter = 0
numCoords = int(turtle.numinput("Coordinates", "Enter Number of Coordinates"))

for i in range(numCoords):
    counter += 1 
    x = int(turtle.numinput("Shapes", f"Enter X {counter}:")).real
    xS.append(x)
    
    y = int(turtle.numinput(F"Shapes", f"Enter Y {counter}:")).real
    yS.append(y)
    

pen.up()
pen.setpos(xS[i],yS[i])
pen.down()

print(xS)
print(yS)

for i in range(numCoords):
   pen.setpos(xS[i],yS[i])
    
   
    
        
     

turtle.done()