"""
Variables in Python:
--------------------
A variable is a container for storing data values. Unlike other programming languages,
Python has no command for declaring a variable. A variable is created the moment 
you first assign a value to it.

Rules for Python Variables:
1. A variable name must start with a letter or the underscore character.
2. A variable name cannot start with a number.
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
4. Variable names are case-sensitive (age, Age and AGE are three different variables).
"""
#Program 1:
name= "Faizan"
age= 17
price= 10.5
print("My name is",name,"My age is",age,"My price is",price)
print(price)
print("My age is:",age)


# Program 2: Creating Variables
print("--- Program 2: Creating and Printing Variables ---")
name = "Ali"       # String variable
age = 25             # Integer variable
height = 5.6         # Float variable
is_student = True    # Boolean variable

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print()  # Print a blank line


# Program 3: Changing Variable Values (Reassignment)
print("--- Program 3: Reassigning Variables ---")
x = 10
print("Original x:", x)

x = 20  # x is now 20
print("New x:", x)

x = "Now I am a string" # Variables can even change type!
print("x as string:", x)
print()


# Program 4: Simple Calculations with Variables
print("--- Program 4: Calculations ---")
apple_price = 2
banana_price = 1
quantity = 5

total_cost = (apple_price + banana_price) * quantity
print("Price of Apple:", apple_price)
print("Price of Banana:", banana_price)
print("Quantity:", quantity)
print("Total Cost:", total_cost)
print()


# Program 5: Assigning Multiple Values
print("--- Program 5: Multiple Assignment ---")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign same value to multiple variables
a = b = c = "Apple"
print("a:", a, "b:", b, "c:", c)
print()


# Program 6: String Concatenation (Combining Strings)
print("--- Program 6: Combining Strings ---")
first_name = "Ali"
last_name = "Ahmad"
full_name = first_name + " " + last_name
print("Full Name:", full_name)
