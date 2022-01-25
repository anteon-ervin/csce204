# Graphical ifs
# Author: Anteon Ervin

import turtle

turtle.bgcolor("antique white")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color()



books = turtle.numinput("Reading Log", "How many books have you read this month: ")

circleSize = 150
style = ("Arial", circleSize-40, "normal")
# $10 Circles
if books >= 30:
    pen.up()
    pen.setpos(0,-circleSize*7/8)
    pen.down()
    pen.fillcolor("dark goldenrod")
    pen.begin_fill()
    pen.circle(circleSize)
    pen.end_fill()

    pen.up()
    pen.setpos(0,-circleSize*3/4)
    pen.down()
    pen.fillcolor("moccasin")
    pen.begin_fill()
    pen.circle(circleSize*7/8)
    pen.end_fill()

    turtle.up()
    turtle.setpos(-circleSize*5/8,-circleSize*1/16)
    turtle.down()
    turtle.color("dark goldenrod")
    turtle.write ("$10", font = style)

# $5 Circles
elif books >= 15:
    pen.up()
    pen.setpos(0,-circleSize*7/8)
    pen.down()
    pen.fillcolor("silver")
    pen.begin_fill()
    pen.circle(circleSize)
    pen.end_fill()

    pen.up()
    pen.setpos(0,-circleSize*3/4)
    pen.down()
    pen.fillcolor("white smoke")
    pen.begin_fill()
    pen.circle(circleSize*7/8)
    pen.end_fill()

    turtle.up()
    turtle.setpos(-circleSize*3/8,-circleSize*1/16)
    turtle.down()
    turtle.color("silver")
    turtle.write ("$5", font = style )


# $2 Circles
elif books >= 5:
    pen.up()
    pen.setpos(0,-circleSize*7/8)
    pen.down()
    pen.fillcolor("sienna")
    pen.begin_fill()
    pen.circle(circleSize)
    pen.end_fill()

    pen.up()
    pen.setpos(0,-circleSize*3/4)
    pen.down()
    pen.fillcolor("peru")
    pen.begin_fill()
    pen.circle(circleSize*7/8)
    pen.end_fill()

    turtle.up()
    turtle.setpos(-circleSize*3/8,-circleSize*1/16)
    turtle.down()
    turtle.color("sienna")
    turtle.write ("$2", font = style )

# $0 Circles
elif books < 5:
    pen.up()
    pen.setpos(0,-circleSize*7/8)
    pen.down()
    pen.fillcolor("red")
    pen.begin_fill()
    pen.circle(circleSize)
    pen.end_fill()

    pen.up()
    pen.setpos(0,-circleSize*3/4)
    pen.down()
    pen.fillcolor("white")
    pen.begin_fill()
    pen.circle(circleSize*7/8)
    pen.end_fill()

    turtle.up()
    turtle.setpos(-circleSize*3/8,-circleSize*1/16)
    turtle.down()
    turtle.color("red")
    turtle.write ("$0", font = style )


turtle.done()