"""
This is a string.
"""
print("Hello")
# Output: Hello


"""
This is also a string even though it has spaces in it.
"""
print("This is also a string")
# Output: This is also a string


"""
"\n" will allow you to create a newline within a string.
"""
print("Here is a newline \n Here is the second line")
# Output: Here is a newline \n Here is the second line


"""
"\t" will allow you to create a tab within your string.
"""
print("Here is the line before the tab \t Here is the second line after the tab")
# Output: Here is the line before the tab \t Here is the second line after the tab


"""
Check the length of a string by doing a length function.

NOTE: This also counts the space within the string.
"""
print(len("Hello World"))
# Output: 11


"""
Printing the string from the variable "s".
"""
s = "Hello World"
print(s)
# Output: Hello World


"""
The indexing point "0" will grab the letter "H" from the string.
"""
a = "Hello World"
print(a[0])
# Output: H


"""
Starts at a designated point.
"""
b = "Hello World"
print(b[1:])
# Output: ello World


"""
Ends at a designated point.
"""
c = "Hello World"
print(c[:3])
# Output: Hel


"""
Grabs the last letter.
"""
d = "Hello World"
print(d[-1])
# Output: d


"""
Grabs everything but the last letter.
"""
e = "Hello World"
print(e[:-1])
# Output: Hello Worl


"""
Grab every other element.
"""
f = "Hello World"
print(f[::2])
# Output: HloWrd


"""
Prints everything backwards.
"""
g = "Hello World"
print(g[::-1])
# Output: dlroW olleH


"""
Prints the letter in the variable letter ten times.
"""
letter = "z"
print(letter*10)
# Output: zzzzzzzzzz


"""
Prints the Hello World in all upper-case letters.
"""
h = "Hello World"
print(h.upper())
# Output: HELLO WORLD


"""
Prints the Hello World in all lower-case letters.
"""
i = "Hello World"
print(i.lower())
# Output: hello world


"""
Splits the string where the space is.
"""
j = "Hello World"
print(j.split(" "))
# Output: ['Hello', 'World']