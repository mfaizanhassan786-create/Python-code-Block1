"""
Data Types in Python:
---------------------
Data types specify the type of value a variable holds. Python is dynamically typed,
meaning you don't need to declare the type explicitly. The interpreter infers it at runtime.

Common Data Types:
1. Text Type:       str (String)
2. Numeric Types:   int (Integer), float (Float), complex
3. Sequence Types:  list, tuple, range
4. Mapping Type:    dict (Dictionary)
5. Set Types:       set, frozenset
6. Boolean Type:    bool (True/False)
7. Binary Types:    bytes, bytearray, memoryview
"""

# Program 1: Basic Data Types (Numbers, Strings, Booleans)
print("--- Program 1: Basic Data Types ---")
x = 10          # int (Integer) - whole number
y = 10.5        # float (Float) - decimal number
z = "Hello"     # str (String) - text
is_active = True # bool (Boolean) - True or False

print("Integer value:", x)
print("Float value:", y)
print("String value:", z)
print("Boolean value:", is_active)
print()


# Program 2: Checking Data Types
print("--- Program 2: Checking Data Types with type() ---")
# The type() function returns the data type of the variable.
val1 = 100
val2 = 99.9
val3 = "Python"

print("Type of val1:", type(val1))  # <class 'int'>
print("Type of val2:", type(val2))  # <class 'float'>
print("Type of val3:", type(val3))  # <class 'str'>
print()


# Program 3: Sequence Types (List, Tuple)
print("--- Program 3: Lists and Tuples ---")
# List: Mutable (changeable), ordered sequence of elements.
my_list = ["Apple", "Banana", "Cherry"]
print("Original List:", my_list)
my_list[0] = "Orange"  # Lists can be changed
print("Modified List:", my_list)

# Tuple: Immutable (unchangeable), ordered sequence of elements.
my_tuple = ("Apple", "Banana", "Cherry")
print("Tuple:", my_tuple)
# my_tuple[0] = "Orange" # This would cause an error!
print()


# Program 4: Mapping Type (Dictionary)
print("--- Program 4: Dictionary ---")
# Dictionary: Key-Value pairs.
student = {
    "name": "Faizan",
    "age": 17,
    "grade": "A"
}
print("Student Dictionary:", student)
print("Student Name:", student["name"])
print("Student Age:", student["age"])
print()


# Program 5: Set Type
print("--- Program 5: Sets ---")
# Set: Unordered collection of unique items.
my_set = {1, 2, 3, 3, 4, 5, 5} # Duplicates are removed automatically
print("Set (duplicates removed):", my_set)

#In the simple and easy exampleis that:

Age2=18
print("My age2 is ",Age2)
print(type(Age2))
print(type(name))
print(type(price))
print(type(age))
