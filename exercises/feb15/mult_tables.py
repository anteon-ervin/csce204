# Tables
# Author: Anteon Ervin

endNum = int(input("Enter how many multiplication tables: "))

# loop through rows
for row in range(1,endNum + 1):
    
    # loop through columns
    for col in range(1,endNum+1):
        if(len(str(row *col)) <2):
            print(f" { row * col} ", end="")
        else:
            print(f"{ row * col} ", end="")
    print() #display a new line