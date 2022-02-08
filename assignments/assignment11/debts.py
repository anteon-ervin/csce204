# Debts
# Author: Anteon Ervin

names = []
debts = []

print("Welcome to Debt Organizer")
while True:
    
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()
    if command =="q":
        break
    elif command == "a":
        name = input("Enter Debt Name: ")
        names.append(name)
        debt = float(input("Enter Debt Amount: "))
        debts.append(debt)
    
    elif command == "v":
        for i in range(len(debts)):
             print(f"- {names[i]}: ${debts[i]}")
    
        
    elif command == "r":
        print("Sorry, people don't really pay off their debts :)")
        
       
    else:   
        print("Invalid Command")

print("Goodbye")