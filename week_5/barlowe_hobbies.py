# Name: Justin Barlowe
# Title: barlowe_hobbies.py
# Description: Exercise 5.3 - Python Conditionals, Lists, and Loops
# Date: 9/5/2023

# Import datetime module
import datetime

# Create lists for hobbies and day of the week
hobbies = ['Gaming', 'Coding', 'hiking', 'TV', 'Music']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Print hobbies
for hobby in hobbies:
    print(f"I enjoy {hobby}")

# Create a variable for the current day of the week
day_index = datetime.datetime.today().weekday()
day = days[day_index]

# If else statement to print if it is a workday or not
if day == 'Saturday' or day == 'Sunday':
    print(f'{day} is a day off, time to enjoy my hobbies!')
else:
    print(f"{day} is a workday")