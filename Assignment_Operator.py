"""
Assignment Operators in Python
------------------------------
Assignment operators are used to assign values to variables.
The most basic one you already know is '='.
But there are "compound" assignment operators that make code shorter.
"""

# Program 1: Basic Assignment (=)
print("--- Program 1: Basic Assignment (=) ---")
x = 10
print("Value of x is:", x)
print()


# Program 2: Add and Assign (+=)
print("--- Program 2: Add and Assign (+=) ---")
score = 50
print("Initial Score:", score)

# Increase score by 10
score += 10 # This is short for: score = score + 10
print("Score after adding 10:", score)
print()


# Program 3: Subtract and Assign (-=)
print("--- Program 3: Subtract and Assign (-=) ---")
money = 100
print("Initial Money:", money)

# Subtract 20 from money
money -= 20 # Does the same as: money = money - 20
print("Money after spending 20:", money)
print()


# Program 4: Other Math Assignments (*=, /=)
print("--- Program 4: Multiply and Divide ---")
num = 5
print("Start:", num)

num *= 2 # Multiplies num by 2
print("After num *= 2:", num) # 10

num /= 5 # Divides num by 5
print("After num /= 5:", num) # 2.0
print()


# Program 5: Advanced Assignments (%=, **=, //=)
print("--- Program 5: Advanced (Assignment) ---")
val = 10
print("Start value:", val)

val %= 3  # Remainder when divided by 3 (10 % 3 = 1)
print("After val %= 3:", val)

original = 5
original **= 2 # 5 to the power of 2 (5 * 5 = 25)
print("5 **= 2 is:", original)

original //= 4 # 25 // 4 = 6 (Floor division)
print("25 //= 4 is:", original)

# Assignment operators are used to assign values to variables.

#Program 6:
a=10
b=20
print(a==b) #Equal to
print(a!=b) #not equal to
a=a+10
print(a)
b=b-10
print(b)
a=a*10
print(a)
b=b/10
print(b)
a=a%10
print(a)
b=b**10
print(b)
a=a//10
print(a)
b=b//10
print(b)

# Or

#Program 7:
a-=10
print(a)
b-=10
print(b)