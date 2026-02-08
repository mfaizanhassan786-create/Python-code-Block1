"""
Relational Operators in Python
------------------------------
Relational operators (or Comparison Operators) are used to compare two values.
They always return a Boolean result: True or False.
This is the way checking conditions in Python.

Key Operators:
- `==`  : Equal to
- `!=`  : Not equal to
- `>`   : Greater than
- `<`   : Less than
- `>=`  : Greater than or equal to
- `<=`  : Less than or equal to
"""

# Program 1: Comparing Numbers
print("--- Program 1: Comparing Numbers ---")
a = 10
b = 5

print(f"a = {a}, b = {b}")
print("Is a greater than b? (a > b):", a > b)    # True
print("Is a less than b? (a < b):", a < b)       # False
print("Is a equal to b? (a == b):", a == b)      # False
print("Is a not equal to b? (a != b):", a != b)  # True
print()


# Program 2: Greater/Less Than or Equal To
print("--- Program 2: Greater/Less Than or Equal ---")
age = 18

print("Age:", age)
print("Is age >= 18?", age >= 18)   # True (because it is equal)
print("Is age <= 10?", age <= 10)   # False
print()


# Program 3: Comparing Strings
print("--- Program 3: Comparing Text ---")
# Python compares strings alphabetically (like a dictionary).

str1 = "Apple"
str2 = "Banana"
str3 = "Apple"

print(f"str1='{str1}', str2='{str2}', str3='{str3}'")
print("Is str1 equal to str3?", str1 == str3)   # True
print("Is str1 equal to str2?", str1 == str2)   # False
print("Is str1 != str2?", str1 != str2)         # True
print()


# Program 4: Real Life Check (Pass or Fail)
print("--- Program 4: Pass or Fail? ---")
passing_marks = 40
my_marks = 35

print(f"Passing Marks: {passing_marks}")
print(f"My Marks: {my_marks}")

# Check if I passed
is_passed = my_marks >= passing_marks
print("Did I pass?", is_passed)

# Comparison operators or relational operators
# Comparison operators are used to compare two values.

#Program 5:
a=20
b=10
print(a<b) #Less than
print(a>b) #Greater than
print(a<=b) #Less than or equal to
print(a>=b) #Greater than or equal to