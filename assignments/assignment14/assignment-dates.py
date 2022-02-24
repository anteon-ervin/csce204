# Assignments 
# Author: Anteon Ervin

from datetime import date, time, datetime

assignments = {"Intro": date(2022, 12, 7),
            "Mad Libs": date(2022, 12, 5), 
            "Bike": date(2022, 12, 8),
            "Prices": date(2022, 2, 12),
            "Lady Bug": date(2022, 2, 24),
            "Zodiac Signs": date(2022, 2, 27),
            "Reading Race": date(2022, 3, 7),
            "Count Factors": date(2022, 3, 15),
            "Hexagon": date(2022, 3, 24),
            "Shoes": date(2022, 3, 28),
              }

# Loop through and display the list of assignments 
counter = 1

today= date.today()
closestDue = date(2022, 12, 31)



for assignmentName in assignments:
    dueDate = assignments[assignmentName]
    daysTillDue = (dueDate - today).days
    
    
    
       
        # if due date already occurred
    
    
    if daysTillDue < 0:
                closestAssignment = f"- {daysTillDue} Days Past Due"
                
            
    elif daysTillDue == 0:
                closestAssignment = f"- Due Today!"
        
    elif daysTillDue <= 15:
                closestAssignment = f" - Due in {daysTillDue} days"
    
    else :
                closestAssignment = ""
    
                
    print(f"- Ass {counter} - {assignmentName} - " + dueDate.strftime(("%b %d, %A"))+ f"{closestAssignment}" )
    counter += 1
            
    
            
    
        
    

