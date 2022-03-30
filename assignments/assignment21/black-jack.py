# Black Jack
# Author : Anteon Ervin

import random
import string


def get_score():
    with open("assignments/assignment21/score.txt")as file:
        lines = file.readlines()
        if not lines:
            return 0 
        return int(lines.pop())
    
def save_score(score):
    with open("assignments/assignment21/score.txt","w")as file:
        file.write(f"{score}")
    
def play_round():
    card = random.randint(1,11)
    total = 0
    score = get_score()
    computerHand = random.randint(14,23)
    print(f"Your Hand Total: {card} ")
    
    
    while True:    
        hit = random.randint(1, 11)
        choice = input(f"Do you want another card (Y)es or (N)o? ").strip().lower()

        if choice == "y":
            print(f"You drew a {hit}.")
            total += hit
            userHand= total + card
            print(f"Your hand totals: {userHand}")
            
            if userHand > 21:
                print(f"Computers hand total: {computerHand}")
                print("You lose")
                break
                
            elif userHand == 21:
                print(f"Computers hand total: {computerHand}")
                print("You win")
                score += 1 
                break
            else:
                continue

        elif choice == 'n':
            print(f"Computers hand total: {computerHand}")
            
            if userHand > computerHand:
                    print("You win")
                    score += 1 
                    break
            elif computerHand > 21:
                    print("You win")
                    score += 1 
                    break
            elif userHand < computerHand:
                    print("You lose")
                    break
            elif userHand == computerHand:
                    print("Tie")
                    break
                
            
            
print("Let's Play Black Jack")

score = get_score()
while True:
    command = input("\n(P)lay or (Q)uit: ").strip().lower()
    
    if command == "q":
        print(f"Your current score is {score}")
        break
    elif command != "p":
        print('Invalid command')
        continue
    
    if play_round():
        
        score += 1 

print("Goodbye")
save_score(score)  

        
            
        
        

  
