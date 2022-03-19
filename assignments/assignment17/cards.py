import random

def compDeal():
   for i in range(1): 
        num = random.randint(1, 13)
        if(num == 1): 
            print(f"Ace"),
            return 1
        elif(num == 2): 
            print("2") 
            return 2
        elif(num == 3): 
            print("3") 
            return 3
        elif(num == 4): 
            print("4") 
            return 4
        elif(num == 5): 
            print("5") 
            return 5
        elif(num == 6): 
            print("6") 
            return 6
        elif(num == 7): 
            print("7") 
            return 7
        elif(num == 8): 
            print("8") 
            return 8
        elif(num == 9): 
            print("9") 
            return 9
        elif(num == 10): 
            print("10") 
            return 10
        elif(num == 11): 
            print("Jack") 
            return 10
        elif(num == 12): 
            print("Queen") 
            return 10
        elif(num == 13): 
            print("King") 
            return 10    
    
def userDeal():
     

    num = random.randint(1, 13)
    if(num == 1): 
        card = print("Ace") 
        return 1
    elif(num == 2): 
        card = print("2") 
        return 2
    elif(num == 3): 
        card = print("3") 
        return 3
    elif(num == 4): 
        card = print("4") 
        return 4
    elif(num == 5): 
        card = print("5") 
        return 5
    elif(num == 6): 
        card = print("6") 
        return 6
    elif(num == 7): 
        card = print("7") 
        return 7
    elif(num == 8): 
        card = print("8") 
        return 8
    elif(num == 9): 
        card = print("9") 
        return 9
    elif(num == 10): 
        card = print("10") 
        return 10
    elif(num == 11): 
        card = print("Jack") 
        return 10
    elif(num == 12): 
        card = print("Queen") 
        return 10
    elif(num == 13): 
        card = print("King") 
        return 10    
  
compDeal = compDeal()
userDeal = userDeal() 

print("Welcome to our Awesome Card Game")
  
while True:
   
    
    print(f"""Computer Deals a Card: {compDeal}""")
    print(f"You deal a Card: {userDeal} ")
    
    compWins = 0
    userWins = 0


    if compDeal > userDeal: 
        print("Computer won this round!")
        compWins += 1
    elif compDeal < userDeal:
        print("You won this round!")
        userWins += 1 
    elif compDeal == userDeal:
        print("Tie")
    
    choice = input("Would you like to play another round (Y)es, (N)o? ")
    
    if choice == "y":
        for i in range(1): 
            {compDeal}
            {userDeal}
            True
    if choice == "n":
        print(f"Your score: {userWins}")
        print(f"Computer Score: {compWins}")
        print("Goodbye")
        break
    
    
    
        
 