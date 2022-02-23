# birthdays
# Author: Anteon Ervin

from datetime import date, time, datetime

birthdays = [date(2022, 3, 22), date(2022, 2, 10), date(2022, 5, 29),
            date(2022, 11, 21), date(2022, 10, 22), date(2022, 3, 12),
            date(2022, 6, 24)]

closestBirthday = date(2022, 12, 31)


for birthday in birthdays:
    daysTillBirthday = (birthday - date.today()).days
    dayTillCurrentClosest = (closestBirthday - date.today()).days
    # if birthday already occurred
    if daysTillBirthday < 0:
        continue
    
    if daysTillBirthday < dayTillCurrentClosest:
        closestBirthday = birthday

print("The closest birthday is " + closestBirthday.strftime("%m/%d/%y") )