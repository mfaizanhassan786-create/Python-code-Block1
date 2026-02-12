# Python Lists
# A list is a collection which is ordered and mutable. Allows duplicate members.
# Lists are created using square brackets [].

# ---------------------------------------------------------
# Example 1: Creating and Accessing Lists
# Creating a list of fruits and accessing elements by index.
# ---------------------------------------------------------
fruits = ["apple", "banana", "cherry", "date"]

print("Original List:", fruits)
print("First fruit:", fruits[0])       # Accessing the first item (Index 0)
print("Last fruit:", fruits[-1])       # Accessing the last item (Index -1)

# Explanation:
# Lists use zero-based indexing. 
# fruits[0] gives "apple".
# Negative indexing starts from the end, so fruits[-1] gives "date".


# ---------------------------------------------------------
# Example 2: Modifying Lists (Adding & Removing)
# Using methods like append(), insert(), remove(), and pop().
# ---------------------------------------------------------
colors = ["red", "green", "blue"]

colors.append("yellow")      # Adds "yellow" to the end
colors.insert(1, "orange")   # Inserts "orange" at index 1
colors.remove("green")       # Removes the first occurrence of "green"
popped_item = colors.pop()   # Removes and returns the last item

print("Modified Colors List:", colors)
print("Popped item:", popped_item)

# Explanation:
# append() adds to the end.
# insert() adds at a specific position.
# remove() deletes a specific value.
# pop() removes the last item if no index is specified.


# ---------------------------------------------------------
# Example 3: Slicing Lists
# Accessing a range of items in a list.
# ---------------------------------------------------------
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

subset1 = numbers[2:6]    # Get items from index 2 up to (but not including) 6
subset2 = numbers[:4]     # Get items from start up to index 4
subset3 = numbers[7:]     # Get items from index 7 to the end
subset4 = numbers[::-1]   # Reverses the list

print("Subset 2-6:", subset1)
print("First 4:", subset2)
print("From 7 onwards:", subset3)
print("Reversed List:", subset4)

# Explanation:
# Slicing uses the format [start:stop:step].
# The stop index is exclusive.


# ---------------------------------------------------------
# Example 4: List Operations (Concatenation, Repetition, Membership)
# Combining lists and checking for values.
# ---------------------------------------------------------
list_a = [1, 2, 3]
list_b = [4, 5, 6]

combined_list = list_a + list_b      # Concatenation
repeated_list = list_a * 2           # Repetition
is_present = 3 in list_a             # Membership check

print("Combined List:", combined_list)
print("Repeated List:", repeated_list)
print("Is 3 in list_a?", is_present)

# Explanation:
# + joins two lists together.
# * repeats the list elements.
# 'in' keyword checks if a value exists in the list (True/False).


# ---------------------------------------------------------
# Example 5: List Comprehension
# A concise way to create lists based on existing lists.
# ---------------------------------------------------------
original_nums = [1, 2, 3, 4, 5]

# Create a new list with squares of the numbers
squares = [x**2 for x in original_nums]

# Create a new list with only even numbers
evens = [x for x in original_nums if x % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)

# Explanation:
# [expression for item in iterable] is the syntax.
# It's a shorthand for a for loop that builds a new list.
# `squares` makes a list of squares.
# `evens` filters the list for even numbers.

#List:

marks = [90,80,70,60,50]
print(marks)
print(type(marks[0]))
print(type(marks))
print("length of list is",len(marks))
print(marks[0])
print(marks[1])
print(marks[2])         
print(marks[3])
print(marks[4])
print(marks[-1])
print(marks[-2])
print(marks[-3])
print(marks[-4])
print(marks[-5])

#Strings are the immutable (cannot be changed) in the python
#Lists are the mutable (can be changed) in the python

student = ["Ahamd",20,"A"]
print(student)
print(type(student[0]))
print(type(student))
print("length of list is",len(student))
print(student[0])
print(student[1])
print(student[2])
print(student[-1])
print(student[-2])
print(student[-3])

#or

student = ["Ahmad", 20, "A"]
print(student)
student[0] = "Ali"
print(student)
student[1] = 21
print(student) #That is allow is the python.
student[2] = "B"
print(student)


#List Slicing:

marks = [90,80,70,60,50]
print("Marks of first 3 students:",marks[0:3])
print("Marks of last 2 students:",marks[-2:])
print("Marks of first 4 student",marks[0:4])


#List Methods:

#append(): Adds an element to the end of the list.
#insert(): Inserts an element at a specific position in the list.
#remove(): Removes the first occurrence of a specific element from the list.
#pop(): Removes and returns the element at a specific position (default is the last element).
#sort(): Sorts the list in ascending order.
#reverse(): Reverses the order of the elements in the list.
#count(): Returns the number of occurrences of a specific element in the list.
#index(): Returns the index of the first occurrence of a specific element in the list.
#copy(): Returns a shallow copy of the list.
#clear(): Removes all elements from the list.

#Append method:

list1 = [90,80,70,60,50]
print(list1)
list1.append(100) 
#If we are print the append function then the return in the result  will be none.
print(list1.append(100))
print(list1)

#Sort method:
#Two types of sort method:
#1. sort(): Sorts the list in ascending order.
#2. sort(reverse=True): Sorts the list in descending order.

list1 = [90,80,70,60,50]
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#Reverse method:

list1 = [90,80,70,60,50]
print(list1)
list1.reverse()
print(list1)

#or

lis2=['a','b','c','d','e']
print(lis2)
lis2.reverse()
print(lis2)

#Count method:

list1 = [90,80,70,60,50]
print(list1)
print(list1.count(90))

#Index method:

list1 = [90,80,70,60,50]
print(list1)
print(list1.index(90))

#Insert method:

list1 = [90,80,70,60,50]
print(list1)
list1.insert(1,100)
print(list1)

#Remove method:

list1 = [90,80,70,60,50]
print(list1)
list1.remove(90)
print(list1)

#Pop method:

list1 = [90,80,70,60,50]
print(list1)
list1.pop()
print(list1)

#or

list1 = [90,80,70,60,50]
print(list1)
list1.pop(1)
print(list1)

#Copy method:

list1 = [90,80,70,60,50]
print(list1)
list1.copy()
print(list1)

#Clear method:

list1 = [90,80,70,60,50]
print(list1)
list1.clear()
print(list1)


