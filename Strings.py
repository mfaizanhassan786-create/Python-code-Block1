"""
Strings in Python
-----------------
A string is just text. You can use single quotes (' ') or double quotes (" ").
"""

# Program 1: Creating Strings
print("--- Program 1: Creating Strings ---")
str1 = 'Hello'
str2 = "World"
print(str1)
print(str2)
print()


# Program 2: String Length
print("--- Program 2: Length of a String ---")
text = "Python"
print("Text:", text)
print("Length:", len(text)) # Counts the letters (6)
print()


# Program 3: Accessing Characters (Indexing)
print("--- Program 3: Indexing ---")
# Computers start counting from 0
word = "Apple"
print("Word:", word)
print("First letter:", word[0]) # A
print("Second letter:", word[1]) # p
print()


# Program 4: Slicing (Cutting Strings)
print("--- Program 4: Slicing ---")
text = "Hello World"
print("Original:", text)
print("First 5 letters:", text[0:5]) # Hello
print()


# Program 5: String Functions
print("--- Program 5: Useful Functions ---")
name = "Faizan Hassan"
print("Original:", name)
print("Upper case:", name.upper())
print("Lower case:", name.lower())
print("Replace:", name.replace("Hassan", "Ali"))
print()


# Program 6: Combining Strings (Concatenation)
print("--- Program 6: Combining Strings ---")
a = "Hello"
b = "Python"
result = a + " " + b
print(result)
print()

#Progra 7: 
name1="Ali"
name2="Ahmad"
name3="Akram"
print("Program no 7 of the Strings.")
print("name1",name1)
print("name2",name2)
print("name3",name3)
print(type(name1))
print(type(name2))
print(type(name3))
