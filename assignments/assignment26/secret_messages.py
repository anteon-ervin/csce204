# Secret Message
# Author : Anteon Ervin


def to_symbols(message):
    
    
    for letter in message:
        print (str(ord(letter)) + ".", end ='')
    print()
    
        
#

def to_letters(symbols):
    
    symbols = symbols.split(".")
    
    for symbol in symbols:
        print (chr(int(symbol.strip())) + "", end ="" )
        
        
        
    print()
   

  
print("Secret Messages!!!")   
while True:
    
    command = input("\n(E)ncode, (D)ecode, or (Q)uit: ").lower()

    if command == 'q':
        break
    if command == 'e':
        message = input("\nEnter a secret message: ").lower()
        print("Your encoded message is:")
        print(f"{to_symbols(message)}")
        
    elif command == 'd':
        symbols = input("\nEnter a encoded message: ")
        print("Your decoded message: ")
        
        print(f"{to_letters(symbols)}")
    else:
    
            print("Invalid command")
print("Goodbye")
