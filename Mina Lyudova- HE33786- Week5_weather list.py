# Week5/A) Write a program to create a 3D list over a week’s weather information
#(e.g., day name (Sunday, Monday, Tuesday, etc), temperature (e.g., 5, 12, 7, 8, etc)
#and outlook of the day(Fogy, Sunny, Cloudy, Cloudy, etc) and use enumerate()
#function with it, and add a new record with the existing list, print it, and delete a
#record and print it agai

#Create Weather list from Mondsay to Sunday

weatherlist = [
    
    ["Monday", 10, "Sunny"],
    ["Tuesday", 7, "Windy"],
    ["Wednesday", 8, "Rainy"],
    ["Thursday", 7, "Cloudy"],
    ["Friday", 11, "Sunny"],
    ["Saturday", 9, "Rainy"],
    ["Sunday", 9, "Windy"],
]

# Print the weather list using enumerate()
print("Original Weather Data:")
for index, day_info in enumerate(weatherlist):
    print(f"{index + 1}. Day: {day_info[0]}, Temperature: {day_info[1]}°C, Outlook: {day_info[2]}")

#Add a new record/ add for next Monday and print again
newday = ["Next Monday", 6, "Sunny/Rainy"]
weatherlist.append(newday)

print("\nAfter Adding a New Record:")
for index, day_info in enumerate(weatherlist):
    print(f"{index + 1}. Day: {day_info[0]}, Temperature: {day_info[1]}°C, Outlook: {day_info[2]}")

#Delete one day from the week and print again (e.g., Wednesday record at index 2)
del weatherlist[2]

print("\nAfter Deleting Wednesday Record:")
for index, day_info in enumerate(weatherlist):
    print(f"{index + 1}. Day: {day_info[0]}, Temperature: {day_info[1]}°C, Outlook: {day_info[2]}")
