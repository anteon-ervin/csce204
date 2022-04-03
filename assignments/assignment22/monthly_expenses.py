# Monthly Expenses
# Author : Anteon Ervin

FILE_NAME = "assignments/assignment22/expenses.txt" 

def readExpenses():
   expenses = {}
   
   with open(FILE_NAME) as file: 
        
    for line in file: 
            line = line.replace(":",":").strip()
            expenses[line] = expenses
    return expenses

def writeExpenses(expenses):
    
    with open(FILE_NAME,"w",) as file:
        for expense in expenses:
            file.write(f'{expense}''\n')
          
            
def listExpenses(expenses):
    
    for expense in expenses:
        
        print(f"{expense}")
        
def addExpenses(expenses):
    
    expenseName = input("Expense: ").strip()
    expenseCost = input("Cost: ")
    expenses[expenseName] = expenseCost
    expenses[expenseCost] = expenseName
    
    
    
    print(f"{expenseName} was added.")
    

while True:
    command = input("\nEnter (L)ist, (A)dd, or (Q)uit: ").lower().strip()
    expenses = readExpenses()
    
    if command == "l":
        listExpenses(expenses)
    elif command == 'a':
        addExpenses(expenses)
    elif command == 'q':
            break
    else:
        print(f"Invalid command, try again")
print("Goodbye")