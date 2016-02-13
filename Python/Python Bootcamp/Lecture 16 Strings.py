# Strings
print("Hello")

# Also a string
print("This is also a string")

"""
\n will allow you to create a newline within a string
"""
print("Here is a newline \n Here is the second line")

"""
\t will allow you to create a tab within your string
"""
print("Here is a newline \t Here is the second line")

# Length
"""
You can check the length of a string by doing a length function
"""
"""
NOTE: This also counts the space within the string
"""

print(len("Hello World"))

# Variables with strings
s = "Hello World"
print(s)

# Indexing
"""
NOTE: Indexing starts at zero so in the example bellow 0 zero would be H
"""
print(s[0])

"""
Starts at a designated point
"""
print(s[1:])

"""
Ends at a designated point
"""
print(s[:3])

"""
Grabs the last letter
"""
print(s[-1])

"""
Grabs everything but the last letter
"""
print(s[:-1])

"""
Grab every other element
"""
print(s[::2])

"""
Prints everything backwards
"""
print(s[::-1])

# Arithmetic with strings
"""
Prints the letter in the variable letter ten times
"""
letter = "z"
print(letter*10)

# String Methods
"""
Prints the Hello World in all uppercase letters
"""
print(s.upper())

"""
Prints the Hello World in all lowercase letters
"""
print(s.lower())

"""
Splits the string where the spaces are
"""
print(s.split(" "))