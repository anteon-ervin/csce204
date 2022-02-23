# Birthdays 2 
# Author: Anteon Ervin

from datetime import date, time, datetime

birthdays = {"Amy": date(2022, 3, 22),
            "Bobby": date(2022, 2, 10), 
            "Carl": date(2022, 5, 29),
            "Dave": date(2022, 11, 21),
            "Erin": date(2022, 10, 22),
            "Fred": date(2022, 3, 2),
            "Gretta": date(2022, 6, 24)}

closestBirthday = date(2022, 12, 31)
closestFriend = ""

for friend in birthdays:
    birthday = birthdays[friend]
    daysTillBirthday = (birthday - date.today()).days
    dayTillCurrentClosest = (closestBirthday - date.today()).days
    # if birthday already occurred
    if daysTillBirthday < 0:
        continue
    
    if daysTillBirthday < dayTillCurrentClosest:
        closestBirthday = birthday
        closestFriend = friend

print(f"The closest birthday is {closestFriend}'s " + closestBirthday.strftime("%m/%d/%y") )