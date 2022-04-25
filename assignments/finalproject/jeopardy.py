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
    questions = getQuestions()
    question = random.choice(list(questions.keys()))   
    turtle.up()
    turtle.setposition(-turtle.window_width()/3,turtle.window_height()/4)
    turtle.down()
    turtle.write(question,move = False, font =("Courier", 40 ,"normal"))
    
def displayAnswer(question):
    questions = getQuestions()
    question = random.choice(list(questions.values()))  
    for letter in question:
        correctLeters.append(letter)
    
    word = ""
    
    for letter in question:
         word += "_" + " "
       
    
    turtle.up()
    turtle.setposition(-turtle.window_width()/3,turtle.window_height()/6)
    turtle.down()
    turtle.write(word,move = False, font =("Courier", 40 ,"normal"))
    
    
  
def displayAnswe(x,y):
  letter = turtle.textinput("Jeopardy","Enter Letter").strip()
  displayQuestion(question)
  word = ""
  for letter in question:
      if letter == correctLeters:
          word += letter + " "
          
      else:
          word += "_" + " "  
          wrongLetters.append(letter)
      
    
  
    



question = getQuestions()
displayQuestion(question)
displayAnswer(question)

turtle.onscreenclick(displayAnswe)

turtle.done()










