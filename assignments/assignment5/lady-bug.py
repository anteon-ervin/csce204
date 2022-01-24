# Graphical Math
# Author: Anteon Ervin

import turtle

turtle.bgcolor()
turtle.setup(950,800)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.hideturtle()

ladyBugBodyinput = turtle.textinput("Lady Bug", "Size (1-10): ").lower().strip()
if ladyBugBodyinput == "1":
    ladyBugBody = 25
if ladyBugBodyinput == "2":
    ladyBugBody = 50
if ladyBugBodyinput == "3":
    ladyBugBody = 75
if ladyBugBodyinput == "4":
    ladyBugBody = 100
if ladyBugBodyinput == "5":
    ladyBugBody = 125
if ladyBugBodyinput == "6":
    ladyBugBody = 150
if ladyBugBodyinput == "7":
    ladyBugBody = 175
if ladyBugBodyinput == "8":
    ladyBugBody = 200
if ladyBugBodyinput == "9":
    ladyBugBody = 225
if ladyBugBodyinput == "10":
    ladyBugBody = 250


    


ladyBugHead = ladyBugBody * 3/4
ladyBugWing = ladyBugBody * 1/16
ladyBugSpots = ladyBugWing *2.5
ladyBugEyes =  ladyBugSpots *7/8

# ladybug head
pen.up()
pen.setpos(-ladyBugHead*1.5,-ladyBugHead)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladyBugHead)
pen.end_fill()

# ladybug body
pen.up()
pen.setpos(0,-ladyBugBody)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladyBugBody)
pen.end_fill()

# ladybug left wing
pen.up()
pen.setpos(ladyBugBody,-ladyBugWing)
pen.down()
pen.setheading(90)
pen.fillcolor("red")
pen.begin_fill()
pen.circle(ladyBugBody,-180)
pen.end_fill()

# ladybug right wing
pen.up()
pen.setpos(ladyBugBody,ladyBugWing)
pen.down()
pen.setheading(90)
pen.fillcolor("red")
pen.begin_fill()
pen.circle(ladyBugBody,180)
pen.end_fill()

# ladybug rightwing spots
pen.up()
pen.setpos(-ladyBugBody*5/8,ladyBugWing*9)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladyBugSpots)
pen.end_fill()

pen.up()
pen.setpos(ladyBugBody*3/8,ladyBugWing*9)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladyBugSpots)
pen.end_fill()

pen.up()
pen.setpos(-ladyBugBody/8,ladyBugWing*5)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladyBugSpots)
pen.end_fill()

# ladybug leftwing spots
pen.up()
pen.setpos(-ladyBugBody*5/8,-ladyBugWing*9)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladyBugSpots)
pen.end_fill()

pen.up()
pen.setpos(ladyBugBody*3/8,-ladyBugWing*9)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladyBugSpots)
pen.end_fill()

pen.up()
pen.setpos(-ladyBugBody/8,-ladyBugWing*5)
pen.down()
pen.fillcolor("black")
pen.begin_fill()
pen.circle(ladyBugSpots)
pen.end_fill()

#ladybug eyes
pen.up()
pen.setpos(-ladyBugHead*2,-ladyBugHead/4)
pen.down()
pen.fillcolor("white")
pen.begin_fill()
pen.circle(ladyBugEyes)
pen.end_fill()

pen.up()
pen.setpos(-ladyBugHead*2,ladyBugHead/4)
pen.down()
pen.fillcolor("white")
pen.begin_fill()
pen.circle(ladyBugEyes)
pen.end_fill()
turtle.done()