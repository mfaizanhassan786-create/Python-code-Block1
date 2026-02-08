"""
Input Function in Python
------------------------
The input() function allows the program to take user input from the keyboard.
By default, input() ALWAYS returns a string (text).
If you want to use numbers, you must convert (cast) them using int() or float().
"""

# Program 1: Basic Input (String)
print("--- Program 1: Asking for Name ---")
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python.")
print("The type of your input is:", type(name))
print()


# Program 2: Input as Integer (Numbers)
print("--- Program 2: Asking for Age (Integer) ---")
# Since input returns a string, we wrap it in int() to make it a number.
age_str = input("Enter your age: ")
age = int(age_str) # Convert text "18" to number 18

print("You are", age, "years old.")
print("Next year you will be", age + 1)
print()


# Program 3: Input as Float (Decimals)
print("--- Program 3: Asking for Price (Decimal) ---")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
print("Total cost is:", total)
print()


# Program 4: A Simple Form
print("--- Program 4: User Profile ---")
# Collecting multiple inputs
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))
user_height = float(input("How tall are you (in meters)? "))

print("\n--- Profile Created ---")
print("Name:", user_name)
print("Age:", user_age)
print("Height:", user_height, "m")

# Input in the Python.

#Program 5:
name=input("Enter your name:")
age=input("Enter your age:")
print("Name:",name)
print("Age:",age)
print("Thanks for Input")

# Another Example:

val=input("Enter any Value:")
print(type(val))
print(val)

# To convert the aproperiate data type.

#Program 6:
a=int(input("Enter any Value:"))
b=float(input("Enter any Value:"))
print(type(a))
print(type(b))

# Anther example is:

name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
marks=float(input("Enter your marks:"))
print("Wellcome",name)
print("Age:",age)
print("Marks:",marks)
print("Thanks for Input")
print(type(name))
print(type(age))
print(type(marks))

#Let's Practice
#Write a program that takes two numbers as input and prints their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum of first and second number is:", num1 + num2)

#Another example is:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum=num1+num2
print("The sum of first and second number is:", sum)

#Let's another example is:
#WAP to input sides of a square and print its area.

side=input("Enter the side of the square: ")
side=int(side)*int(side)
print("The area of the square is:",side)
print(type(side))

#Another example is:

#Program 7:
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("The sum of first and second number is:",num1+num2)
print("The difference of first and second number is:",num1-num2)
print("The product of first and second number is:",num1*num2)
print("The division of first and second number is:",num1/num2)
print("The modulus of first and second number is:",num1%num2)
print("The exponentiation of first and second number is:",num1**num2)
print("The floor division of first and second number is:",num1//num2)
print(type(num1))
print(type(num2))
