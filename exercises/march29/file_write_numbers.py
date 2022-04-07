numbers = [3,4,85,23,54]

with open("exercises/march29/numbers.txt","a")as file:
    for number in numbers:
        file.write(f"{number}\n")