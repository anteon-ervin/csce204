from question import Question
import random

def get_questions():
    questions = []
    with open("exercises/april4/questions.txt") as file:
            for line in file:
                data = line.split(",") 
                prompt = data[0].strip()
                answer1 = data[1].strip()
                answer2 = data[2].strip()
                answer3 = data[3].strip()
                answer4 = data[4].strip()
                correct_ans = int(data[5].strip())
                questions.append(Question(prompt, answer1, answer2, answer3, answer4, correct_ans))
    return questions
questions = get_questions()

print("Welcome to our Trivia Game!")

while True:
    command = input("Would you like to (P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        break
    if command != "p":
        print(("Invalid input"))
        continue

    question = random.choice(questions)
    print("\n" + question.prompt)
    question.display_answers()
    
    user_ans = int(input("Enter numberical answer: "))

    if question.is_correct(user_ans):
        print("Nicely done!")

    else:
        print("Sorry, wrong answer, correct answer is: {quest.correct_answer + 1}")

print("Goodbye")