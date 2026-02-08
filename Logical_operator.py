"""
Logical Operators in Python
---------------------------
Logical operators are used to combine multiple conditions.
There are three main logical operators:
1. `and` : Returns True if BOTH statements are true.
2. `or`  : Returns True if AT LEAST ONE statement is true.
3. `not` : Reverses the result (returns False if the result is true).

"""

# Program 1: The 'and' Operator
print("--- Program 1: The 'and' Operator ---")
# Rule: Both conditions must be True.
print("True and True is:", True and True)     # True
print("True and False is:", True and False)   # False
print("False and False is:", False and False) # False

# Example: To pass, you must study AND complete assignments.
studied = True
completed_assignments = True
passed = studied and completed_assignments
print("Did I pass?", passed)
print()


# Program 2: The 'or' Operator
print("--- Program 2: The 'or' Operator ---")
# Rule: Only one condition needs to be True.
print("True or False is:", True or False)     # True
print("False or False is:", False or False)   # False

# Example: You can pay with Cash OR Credit Card.
has_cash = False
has_credit_card = True
can_pay = has_cash or has_credit_card
print("Can I pay?", can_pay)
print()


# Program 3: The 'not' Operator
print("--- Program 3: The 'not' Operator ---")
# Rule: Flips the boolean value.
is_raining = True
print("Is it raining?", is_raining)
print("Is it NOT raining?", not is_raining)   # False

# Example: If not busy, I can play.
is_busy = False
can_play = not is_busy # True (because busy is False)
print("Can I play?", can_play)
print()


# Program 4: Real Life Login Check
print("--- Program 4: Login Check ---")
username = "admin"
password = "123"

# User input simulation
input_user = "admin"
input_pass = "123"

# Check if BOTH username AND password match
is_logged_in = (input_user == username) and (input_pass == password)
print(f"Login attempt for user '{input_user}': {is_logged_in}")

# Logical operators are used to combine conditional statements.

#Program 5:
a=True
b=False
print(a and b)
print(a or b)
print(not a)
print(not b)

#Another Example:

val1=True
val2=False
print(val1 and val2)
print(val1 or val2)
print(not val1)
print(not val2)

# Membership operators
# Membership operators are used to test if a sequence is presented in an object.

#Program 6:
a="Faizan"
b="Hassan"
print("Faizan" in a)
print("Hassan" in b)
print("Faizan" not in a)
print("Hassan" not in b)

# type conversion
# Type conversion have two types:
# Type conversion.

#Progam 7:
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# Type Casting.

#Program 8:
a=float("2")
b=4.40
print(type(a))
print(type(b))
print(a+b)
