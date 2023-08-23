# Name: Justin Barlowe
# Title: Barlowe_calculator.py
# Description: Python Calculator Application
# Date: 8/23/2023


# Add function
def add(x, y):
    return x + y


# Subtract function
def subtract(x, y):
    return x - y

# Divide function
def divide(x, y):
    if y!= 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"
    
# Multiply function
def multiply(x, y):
    return x * y

# Test values
num1 = 20
num2 = 5

# String concatenation
add_result = str(num1) + " + " + str(num2) + " is " + str(add(num1, num2))
subtract_result = str(num1) + " - " + str(num2) + " is " + str(subtract(num1, num2))
divide_result = str(num1) + " / " + str(num2) + " is " + str(divide(num1, num2))
multiply_result = str(num1) + " * " + str(num2) + " is " + str(multiply(num1, num2))

# Print results
print(add_result)
print(subtract_result)
print(divide_result)
print(multiply_result)