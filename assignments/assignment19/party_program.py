# Party list
# Author: Anteon Ervin

def getBoolean(item):
    
        if item == "true":
            return True
        elif item == "false":
            return False
        
def getGuests():
    getGuests = {}
    with open("assignments/assignment19/guest_list.txt") as file:
            for line in file:
                data = line.split(':')
                names = data[0].strip()
                value = data[1].strip()
                getGuests[names] = getBoolean(value)   
                
            return getGuests
             
def displayGuests(guests,coming):
       for person in guests:
        if coming == guests[person]:
                print(f"{person}")
        elif coming == guests[person]:
                print(f"{person}")
item = getGuests()
guests = getGuests()
print("Let's Plan ur Party")
while True:
    choice = input(f"\nView (A)ttending, (N)ot attending, or (Q)uit: ").lower().strip()


    if choice == "a":
                print("\nAttending Guest List:")
                
                print(f"{displayGuests(guests,True)} ")

    elif choice == "n":
            print("\nNot-Attending Guest List:")
        
            print(f"{displayGuests(guests,False)}")
    
    elif choice == 'q':
            print("Goodbye")
            break

        
    
                
            