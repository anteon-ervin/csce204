# List2
# Author: Anteon Ervin

toys = ["doll", "rope", "car","truck","shovel"]
print("Welcome to our toy store")
while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").lower().strip()

    if command =="q":
        break
    elif command == "v":
        for toys in toys:
            print(f"- {toys}")
    elif command == "a":
        toy = input("Enter toy: ")
        toys.append(toy)
    elif command == "r":
        toy = input("Enter toy: ")
        toys.remove(toy)
    else:   
        print("Invalid Command")

print("goodbye")

