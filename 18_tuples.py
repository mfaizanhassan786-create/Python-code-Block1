# Python Tuples
# A tuple is a collection which is ordered and immutable (unchangeable).
# Tuples are written with round brackets ().

# ---------------------------------------------------------
# Example 1: Creating and Accessing Tuples
# Creating a tuple of coordinates and accessing values.
# ---------------------------------------------------------
coordinates = (10, 20, 30)

print("CoordinatesTuple:", coordinates)
print("First Element:", coordinates[0])
print("Last Element:", coordinates[-1])

# Explanation:
# Tuples use zero-based indexing like lists.
# coordinates[0] accesses the first element.
# coordinates[-1] accesses the last element.


# ---------------------------------------------------------
# Example 2: Immutability Check
# Demonstrating that tuples cannot be changed after creation.
# ---------------------------------------------------------
my_tuple = ("apple", "banana", "cherry")

print("\nOriginal Tuple:", my_tuple)
# my_tuple[1] = "orange"  # Uncommenting this line would cause a TypeError
print("Tuples are immutable, so we cannot change 'banana' to 'orange'.")

# Explanation:
# Unlike lists, tuples are immutable. 
# Trying to assign a new value to an index (my_tuple[1] = ...) raises a TypeError.


# ---------------------------------------------------------
# Example 3: Tuple Unpacking
# Extracting values back into variables.
# ---------------------------------------------------------
student_info = ("John", 25, "Computer Science")

name, age, course = student_info

print("\nName:", name)
print("Age:", age)
print("Course:", course)

# Explanation:
# You can assign a tuple to multiple variables in one line.
# This is called unpacking. The number of variables must match the tuple length.


# ---------------------------------------------------------
# Example 4: Tuple Methods (Count & Index)
# Using built-in methods for tuples.
# ---------------------------------------------------------
numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 7)

count_seven = numbers.count(7)
index_of_eight = numbers.index(8)

print("\nCount of 7:", count_seven)
print("Index of first 8:", index_of_eight)

# Explanation:
# count() returns the number of times a value appears.
# index() finds the index of the first occurrence of the specified value.


# ---------------------------------------------------------
# Example 5: Single Item Tuple & Length
# How to create a tuple with one item and check length.
# ---------------------------------------------------------
single_item_tuple = ("hello",) # Note the comma
not_a_tuple = ("hello")        # This is just a string

print("\nType with comma:", type(single_item_tuple))
print("Type without comma:", type(not_a_tuple))
print("Length of numbers tuple:", len(numbers))

# Explanation:
# To create a tuple with only one item, you must add a comma after the item, 
# otherwise Python will not recognize it as a tuple.

#And

#Tuples:

# Tuples are immutable, which means they cannot be changed after creation.
# Tuples are ordered collections of elements.
# Tuples are defined using parentheses ().
# Tuples can contain elements of different data types.
# Tuples are more memory-efficient than lists.
# Tuples are faster than lists.
# Tuples are immutable, which means they cannot be changed after creation.
# Tuples are ordered collections of elements.
# Tuples are defined using parentheses ().
# Tuples can contain elements of different data types.
# Tuples are more memory-efficient than lists.
# Tuples are faster than lists.


#Tuple Methods:

tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-1])
print(tup[-2])
print(tup[-3])
print(tup[-4])
print(tup[-5])

#or

tup = ("Hello")
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-1])
print(tup[-2])
print(tup[-3])
print(tup[-4])
print(tup[-5])


#Note: If we are print the tuple without parentheses then the return in the result  will be string.
#Note: If we are print the tuple with parentheses then the return in the result  will be tuple.

#or

tup = ("Hello",)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0])

#Slicing:

tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))
print(tup[0:3])
print(tup[-2:])
print(tup[0:4])



#count(): Returns the number of occurrences of a specific element in the tuple.
#index(): Returns the index of the first occurrence of a specific element in the tuple.

#Index method:

tup = (1,2,3,4,5)
print(tup)
print(type(tup))
print(len(tup))
print(tup.index(3))

#Count method:

tup = (1,2,3,4,5,1,4)
print(tup)
print(type(tup))
print(len(tup))
print(tup.count(1))