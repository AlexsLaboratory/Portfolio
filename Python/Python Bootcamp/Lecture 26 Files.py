"""
Reading a text file.
"""
file = open("test (Lecture 26 Files).txt")
print(file.read())
# Resets the "read head" back to the beginning of the text file so that it can print it out again. 
file.seek(0)
# Prints out the whole text file as a list. NOTE: The only caveat is that python stores the list entirely in memory.
print(file.readlines())
file.seek(0)
print(file.read())
# Output:
"""
First line
Second line
First line
Second line
"""


"""
Iterating through a text file.
"""
for text in open("test (Lecture 26 Files).txt"):
	print(text)
# Output:
"""
First line

Second line
"""