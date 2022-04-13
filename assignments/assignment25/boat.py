#Boat
# Author: Anteon Ervin
class Boat:
    def __init__(self, x, y, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.color = color
        
    def draw(self, pen):
        pen.up()
        pen.setpos(self.x - self.height/2, self.y - self.height/2)
        pen.down()
        pen.fillcolor(self.color)
        pen.pencolor(self.color)
        
        self.draw_frame(pen)
        self.draw_flag(pen)
        self.draw_pole(pen)
        
        
    
    def draw_frame(self, pen):
    
        width = self.height
        pen.begin_fill()
        pen.forward(180/width*2)
        pen.left(-120)
        pen.forward(80/width*2)
        pen.left(-60)
        pen.forward(100/width*2)
        pen.left(-60)
        pen.forward(80/width*2)
        pen.end_fill()
    

    def draw_pole(self, pen):
        width = self.height 
        pen.up()
        pen.setheading(90)
        pen.pensize(4)
        pen.setpos(self.x + self.height*18, self.y )
        pen.down()
        pen.pencolor("saddle brown")
        pen.forward(180/width)
        pen.setheading(0)
        
    def draw_flag(self, pen):
        width = self.height 

        pen.up()
        pen.setheading(90)
        pen.setpos(self.x + self.height*18 , self.y + self.height + 100/width)
        pen.down()
        pen.begin_fill()
        for i in range(3):
            pen.forward(60/width)
            pen.left(120)
        pen.end_fill()
        pen.setheading(0)
    
  