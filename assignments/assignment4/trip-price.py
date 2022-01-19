# Math
# Author: Anteon Ervin

print(f"Let's see how expensive your trip will be")

miles = float(input("How many miles will you travel: "))
days = float(input("How many days will you be travelling: "))

gasPrice = miles / 24.9 * 3.159

breakfastCost = days * 10
lunchCost = days * 12.50 
dinnerCost = days * 20.0
hotelCost = days * 103.25

travelCost = hotelCost + dinnerCost + lunchCost + breakfastCost + gasPrice

print(F"Travel cost: ${round(travelCost,2)}")