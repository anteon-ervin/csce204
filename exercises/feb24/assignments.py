# Assignments 
# Author: Anteon Ervin

from datetime import date, time, datetime

assignments = {"Python Intro": date(2022, 1, 22),
            "Learning Math": date(2022, 1, 30), 
            "If Statements": date(2022, 2, 5),
            "While Loops": date(2022, 2, 14),
            "For Loops": date(2022, 2, 27),
            "Lists": date(2022, 3, 2),
            "Tuples": date(2022, 3, 7)}

# Loop through and display the list of assignments 
counter = 1

for assignment in assignments:
    dueDate = assignments[assignment]
    print(f"{counter}. {assignment} - Due: " + dueDate.strftime(("%m/%d/%y")) )
    counter += 1

