# Jeopardy
# Author : Anteon Ervin
import random
import turtle

from question import Question

turtle.setup(600,600)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def getQuestions():
        questions = {}
        with open("assignments/finalproject/questions.txt") as file:
                for line in file:
                    data = line.split(":") 
                    question = data[0].strip()
                    answer = data[1].strip()
                    questions[question]= answer
        return questions
            


wrongLetters = []
correctLeters = []


def displayQuestion(question):
    global questions
    questions = getQuestions()
    
    question = random.choice(list(questions.keys()))   
    turtle.up()
    turtle.setposition(-turtle.window_width()/3,turtle.window_height()/4)
    turtle.down()
    turtle.write(question,move = False, font =("Courier", 30 ,"normal"))
    
def displayAnswer(question):
    questions = getQuestions()
    displayQuestion(question)
    global answer  
    for letter in answer:
        #correctLeters.append(letter)
        if letter not in answer:
         wrongLetters.append(letter)
        
    word = ""
    
    for letter in answer:
        if letter in correctLeters:
            word += letter + " "
        else:
                word += "_" + " "
       
    
    turtle.up()
    turtle.setposition(-turtle.window_width()/3,turtle.window_height()/6)
    turtle.down()
    turtle.write(word,move = False, font =("Courier", 30 ,"normal"))
    
    
    
  
def displayGuess(x,y):
        
        letter = turtle.textinput("Jeopardy","Enter Letter")
        global answer
        
        word = ""
        for letter in answer:
            if letter in correctLeters:
                if correctLeters == "_":
                    word += letter + ""
                    turtle.up()
                    turtle.setposition(-turtle.window_width()/3,turtle.window_height()/6)
                    turtle.down()
                    turtle.write(word,move = True, font =("Courier", 30 ,"normal"))
                    
                else:
                    word += letter + " "
                    turtle.up()
                    turtle.setposition(-turtle.window_width()/3,turtle.window_height()/12)
                    turtle.down()
                    turtle.write("INCORRECT:",move = False, font =("Courier", 30 ,"normal"))
                    turtle.up()
                    turtle.setposition(-turtle.window_width()/3,turtle.window_height()/18)
                    turtle.down()
                    turtle.write('',move = False, font =("Courier", 30 ,"normal"))

                
                
            
        

question = getQuestions()

answer = random.choice(list(question.values()))
displayAnswer(question)

turtle.onscreenclick(displayGuess)

def drawFlower():
    pen.up()
    pen.setheading(270)
    pen.setposition(0,0)
    pen.down()
    pen.pencolor("green")
    pen.forward(50) 

    #pedals
    pen.up()
    pen.setheading(0)
    pen.setposition(0,0)
    pen.down()
    pen.pencolor("red")
    for i in range (30):
        pen.circle(50,60)
        if i % 2 ==0:
            pen.circle(0,100)
    pen.setheading(0)

def drawCar():
        draw_body(x, y)
        draw_tire(x-carWidth/4.5, y-carWidth/4)
        draw_tire(x+carWidth/4.5, y-carWidth/1.7)

        carWidth = 100


        color = random.choice(colors)
        pen.up()
        pen.setpos(x-carWidth/2,y-carWidth/4)
        pen.down()
        pen.color(color)
        pen.fillcolor(color)
        pen.begin_fill()
        pen.forward(carWidth)
        pen.left(90)
        pen.forward(carWidth/3)
        pen.left(90)
        pen.forward(carWidth)
        pen.end_fill()

        tireRadius = carWidth/6

        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.fillcolor("black")
        pen.begin_fill()
        pen.circle(tireRadius)
        pen.end_fill()
        pen.setheading(0)


        lineLength = 90
        x = -turtle.window_width()/2
        for i in range(8):
            pen.color("yellow")
            pen.up()
            pen.setpos(x,0)
            pen.down()
            pen.forward(lineLength)
        x += 100

def rainbow():
    colors = ("violet", "indigo", "blue", "green","yellow", "orange","red")
    arcLength = 200
    counter = 0
    for color in colors:
        pen.up()
        pen.setpos(-arcLength,counter * 10)
        pen.down()
        pen.color(color)
        pen.setheading(60)
        pen.circle(-arcLength,120)
        counter += 1

turtle.done()










