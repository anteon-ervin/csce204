# Exams
# Author: Anteon Ervin

from datetime import date, time, datetime

todayExams = []
futureExams = []
exams = {"CSCE 100": datetime(2022,4,12 ,8,30),
            "CSCE 101": datetime(2022, 4, 5 ,15,0), 
            "CSCE 102": datetime(2022, 4, 8 ,9,0),
            "CSCE 103": datetime(2022, 2, 24 ,12,0),
            "CSCE 104": datetime(2022, 2, 24 ,15,30),
            "CSCE 105": datetime(2022, 2, 27 ,14,30),
            "CSCE 106": datetime(2022, 3, 7 ,13,0),
        }





for examName in exams:
    theDate = exams[examName]
    
    if datetime.today().date() == theDate.date():
        today = (f""+ theDate.strftime(("%I:%M %p"))+ f" {examName}")
        todayExams.append(today)
        
        
    if datetime.today().date() < theDate.date():
        future = (f""+ theDate.strftime(("%I:%M %p"))+ f" {examName}")
        futureExams.append(future)

print("Todays Exams:")
for today in todayExams:        
    print(today)

print(f"""
Upcoming Exams:""")
for future in futureExams:
 print(future)
         