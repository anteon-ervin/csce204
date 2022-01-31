# Factors
# Author: Anteon Ervin

print("Let's Count Factors")
number = int(input("Enter Number: "))

for i in range(1,number+1):
   if(number%i == 0):
       print(f"{i}")
   