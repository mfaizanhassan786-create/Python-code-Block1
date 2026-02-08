"""
Booleans in Python
------------------
Booleans represent one of two values: True or False.
They are very important for making decisions in programming.
"""

# Program 1: Creating Booleans
print("--- Program 1: What is a Boolean? ---")
is_sunny = True
is_raining = False

print("Is it sunny?", is_sunny)
print("Is it raining?", is_raining)
print("Type of is_sunny:", type(is_sunny))
print()


# Program 2: Comparison (Greater or Less)
print("--- Program 2: Comparing Numbers ---")
# When you compare two numbers, Python gives you a Boolean answer.
x = 10
y = 5

print("Is 10 greater than 5?", x > y)  # True
print("Is 10 less than 5?", x < y)     # False
print("Is 10 equal to 5?", x == y)     # False
print()


# Program 3: Simple Logic
print("--- Program 3: Simple Logic (and, or, not) ---")
a = True
b = False

# AND: Both must be True
print("True and False is:", a and b)

# OR: At least one must be True
print("True or False is:", a or b)

# NOT: Reverses the value
print("Not True is:", not a)
print()


# Program 4: Using bool() function
print("--- Program 4: The bool() Function ---")
# Almost everything is True if it has some content.
# Empty strings, 0, and None are False.

print("Is 'Hello' True?", bool("Hello"))
print("Is 15 True?", bool(15))

print("Is 0 True?", bool(0))        # False
print("Is empty string True?", bool("")) # False
print()


# Program 5: Real Life Example
print("--- Program 5: Can I Vote? ---")
age = 18
has_id = True

# Logical condition: age must be 18+ AND must have ID
can_vote = (age >= 18) and has_id

print("Age:", age)
print("Has ID:", has_id)
print("Can vote?", can_vote)

#Program 6: Age Example:
age=17
old=False
a=None
print(type(old))
print(type(a))
print(type(age))

# Python is a case sensitive Language.

