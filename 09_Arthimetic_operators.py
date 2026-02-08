"""
Arithmetic Operators in Python
------------------------------
Arithmetic operators are used to perform common mathematical operations.
"""

# Program 1: Basic Math (Plus, Minus, Multiply, Divide)
print("--- Program 1: Basic Math ---")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print("Addition (a + b):", a + b)       # 13
print("Subtraction (a - b):", a - b)    # 7
print("Multiplication (a * b):", a * b) # 30
print("Division (a / b):", a / b)       # 3.333... (Result is always a float)
print()


# Program 2: The Remainder (Modulus)
print("--- Program 2: Modulus (%) ---")
# The % operator gives the remainder of a division.
# Very useful for checking even/odd numbers.

print("10 divided by 3 has a remainder of:", 10 % 3) # 10 = 3*3 + 1
print("20 divided by 5 has a remainder of:", 20 % 5) # 20 = 5*4 + 0
print()


# Program 3: Power (Exponentiation)
print("--- Program 3: Power (**) ---")
# Use ** to raise a number to a power.

x = 2
y = 3
print(f"{x} to the power of {y} (2^3) is:", x ** y) # 2 * 2 * 2 = 8
print()


# Program 4: Floor Division (Integer Division)
print("--- Program 4: Floor Division (//) ---")
# The // operator divides and rounds DOWN to the nearest whole number.
# It chops off the decimal part.

val1 = 10
val2 = 3
print("Normal Division (10 / 3):", val1 / val2)     # 3.3333...
print("Floor Division ( 10 // 3):", val1 // val2)   # 3
print()


# Program 5: A Simple Calculator
print("--- Program 5: Simple Calculator ---")
num1 = 50
num2 = 10

sum_val = num1 + num2
diff_val = num1 - num2
prod_val = num1 * num2
div_val  = num1 / num2

print("Numbers:", num1, "and", num2)
print("Sum:", sum_val)
print("Difference:", diff_val)
print("Product:", prod_val)
print("Division:", div_val)

#Program 6: Mix Operators

a=5
b=2
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a%b) #Modulus
print(a**b) #Exponentiation
print(a//b) #Floor division