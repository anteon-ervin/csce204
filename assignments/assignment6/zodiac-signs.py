# if statements
# Author: Anteon Ervin

firstChoice = input(f"""
***** Monthly Fortune Telling *****
What would you like to do? (V)iew signs, or see class (F)ortune: """).lower().strip()

if firstChoice == "v": 
    print(f"""
    Astrological Signs and Dates: 
    - Aries: March 21 - April 19
    - Taurus: April 20 - May 20
    - Gemini: May 21 - June 21
    - Cancer: June 22 - July 22
    - Leo: July 23 - August 22
    - Virgo: August 23 - September 22
    - Libra: September 23 - October 23
    - Scorpius: October 24 - November 21
    - Sagittarius: November 22 - December 21
    - Capricoronus: December 22 - January 19
    - Aquarius: January 20 - February 18
    - Pisces: February 19 - March 20 """)

elif firstChoice == "f":
    sign = input("Enter your sign: ").lower().strip()
    
    if sign == "aries": 
        print(f"""You often use your head in tough situations.
Have a nice day""")
        
    elif sign == "taurus":
        print(f"""You are as strong as a bull!
Have a nice day""")
        
    elif sign == "gemini":
        print(f"""You are very socialable and intellectual.
Have a nice day""")

    elif sign == "cancer":
        print(f"""You are very caring.
Have a nice day""")

    elif sign == "leo":
        print(f"""You are as brave as a lion!
Have a nice day""")

    elif sign == "virgo":
        print(f"""You would be a great professor!
Have a nice day""")

    elif sign == "capricornus":
        print(f"""You are the G.O.A.T!... and fish.
Have a nice day""")

    elif sign == "scorpio":
        print(f"""You are very discreet but pack a strong punch!
Have a nice day """)

    elif sign == "sagittarius":
        print(f"""You are very outspoken and humorous.
Have a nice day""")

    elif sign == "libra":
        print(f"""You are the best of the best, 10/10 in all traits!
Have a nice day""")

    elif sign == "aquarius":
        print(f"""You are free-spirited and often fight for a cause.
Have a nice day""")

    elif sign == "pisces":
        print(f"""You are very emotional but also sympathetic to others.
Have a nice day""")

    else:
        print(f"""Sorry {sign} is an invalid command.
Have a nice day""")

else:
    print(f"""Sorry {firstChoice} is an invalid command.
Have a nice day""")


    
    


