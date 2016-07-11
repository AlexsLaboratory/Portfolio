

# Sets


"""
Think of sets as an unordered list of unique elements.

NOTE: In the example below notice that is only printed out 1 once because it was already in the set.
"""
x = set()
x.add(1)
x.add(2)
x.add(1)
print(x)
# Output: {1, 2}


"""
Example of a good use case for only getting the unique elements out of a list.

NOTE: It is only going to grab all of the unique elements.
"""
l = [1,1,1,1,2,2,2,2,3,3,3,4]
print(set(l))
# Output: {1, 2, 3, 4}


# Booleans


"""
Booleans have two possible values which can either be True or False.
"""
a = True
print(a)
# Output: True


print(1 > 2)
# Output: False


print(10 > 2)
# Output: True


"""
You can also set a variable to None as a place holder.
"""
a = None
print(a)
# Output: None