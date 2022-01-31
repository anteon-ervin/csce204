# Answering Game
# Author: Anteon Ervin

import random



    
print(f"Welcome to our Question Answer Game ")
question = input(f"Ask a yes or no question: ")
num = random.randint(1, 3)
if num == 1:
   answer = print("Yes")
elif num == 2:
    answer = print("No")
elif num == 3:
   answer = print("Maybe")
   
command = input(f"""Would you like to ask another question? (Y)es or (N)o:""").lower().strip()
while command =="y":
    question = input(f"Ask a yes or no question: ")
    num = random.randint(1, 3)
    if num == 1:
       answer = print("Yes")
    elif num == 2:
        answer = print("No")
    elif num == 3:
        answer = print("Maybe")  
    
    command = input(f"Would you like to ask another question? (Y)es or (N)o: ").lower().strip()
    
print("Goodbye")


