# Shoes
# Author: Anteon Ervin

shoes = []
print("Shoe Inventory")

while True:
    shoe = input("Enter Shoe Name: ")
    shoes.append(shoe)
    command = input("Do you have more shoes to add, (Y)es or (N)o: ").lower().strip()
    
    if command =="n":
        print(f"Here's your shoe inventory list: ")
        for shoe in shoes:
         print(f"- {shoe}")
        break
    elif command == "y":
        True
    else:   
        print("Invalid Command")