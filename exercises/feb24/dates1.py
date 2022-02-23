# Dates
# Author: Anteon Ervin

from datetime import date, time, datetime

todaysDate = date.today()

print(todaysDate)
print(todaysDate.strftime("%m/%d/%y"))
print(todaysDate.strftime("%A %B %d, %Y"))

todaysDateTime = datetime.now()
print(todaysDateTime.strftime("%A %B %d, %Y: %I:%M %p"))

halloween = date(2021, 10, 21)
meeting = time(14, 30) 
appointment = datetime(2021, 3, 1, 14, 30)

#birthdate.program
dateEntered = input("Enter birthday (MM/DD/YYYY)").strip()
birthDate = datetime.strptime(dateEntered, "%m/%d/%Y")

print("Your birthday is " + birthDate.strftime("%B %d"))

# how long till your appointment 
days = (appointment - datetime.now()).days
print(f"You have {days} till your appointment")

