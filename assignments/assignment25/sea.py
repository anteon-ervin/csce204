from boat import Boat
import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
turtle.bgcolor("sky blue")
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
colors = ("violet", "indigo", "blue", "green","yellow", "orange","red")


for i in range(10):
    x = random.randint(-int(turtle.window_width()/2),int(turtle.window_height()/2))
    y = random.randint(-int(turtle.window_height()/2),int(turtle.window_width()/2))
    height = random.randint(2, 4)
    color = random.choice(colors)
    myBoat = Boat(x, y, height, color)
    myBoat.draw(pen)

turtle.done()