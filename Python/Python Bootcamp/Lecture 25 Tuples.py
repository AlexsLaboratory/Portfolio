"""
Creating a tuple.
"""
tup = (1, 2, 3)
print(tup)
# Output: (1, 2, 3)


"""
You can have mixed object types such as strings, integers, and floating point numbers.
"""
tup1 = ("one", 2, 3.1)
print(tup1)
# Output: ('one', 2, 3.1)


"""
Indexing a tuple.
"""
tup2 = ("one", "two", 3)
print(tup2[1])
# Output: two


"""
Printing out specific parts of a tuple.
"""
tup3 = ("one", "one", 2, 3.1)

# Returns the index number of a specific object.
print(tup3.index(3.1))
# Output: 3

# Returns a number of how many times that object shows up in the tuple.
print(tup3.count("one"))
# Output: 2


"""
Proving that tuples are immutable
"""
tup4 = (1, 2, 3)
tup4[1] = "s"
# Output: tup4[1] = "s" TypeError: 'tuple' object does not support item assignment