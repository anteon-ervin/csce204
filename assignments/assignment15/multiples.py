# Finding Factors
# Author: Anteon Ervin

def displayMultiples(num):
    answers = []
    
    if num < 0:
        print("Invalid number")
        return
    
    for answer in range(1, 101):
        
        if(answer%num == 0):
            
            answers.append(answer)
    
        
    print(*answers)
    
while True:
    command = input("(L)ist Multiples, or (Q)uit: ")

    if command ==  "q":
        print("Goodbye")
        break
    elif command == "l":
       num = int(input("Enter Number: "))
       displayMultiples(num)
    
    else:
        print("Invaild command")
    
    



