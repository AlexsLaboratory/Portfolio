"""
Lists can hold any object type such as integers, floating points and strings.
"""
my_list = ["one","two","three",4, 4.5]
print(my_list)


"""
The len function also works with lists and will count how many elements there are in the list
"""
print(len(my_list))


"""
Lists can be indexed just like a string can.
"""
my_list2 = ["one","two","three",4,5]
print(my_list2[0])
print(my_list2[1:])
print(my_list2[:2])
print(my_list2[::-1])


"""
You can concatenate lists with other lists. This does not change either of the variables.
"""
print(my_list + my_list2)


"""
You can permanently add one list to another list. This does change the variables.
"""
my_list = my_list + my_list2
print(my_list)


"""
You can multiply list too. This will print your list 8 times and make it only one list.
"""
print(my_list * 8)


"""
You can append attributes onto lists
"""
my_list3 = ["one","two",3,3.5]
print(my_list3)
my_list3.append("I am appended")
print(my_list3)


"""
You can you another method called pop which will "pop" off by default the last index of the list
"""
print(my_list.pop(0))
print(my_list)


"""
You can reverse the order of a list with the reverse function
"""
new_list = ["g","m","p","a","t"]
print(new_list)
new_list.reverse()
print(new_list)

"""
You can also sort the order of a list. It will sort numbers by ascending order and will sort letters by alphabetical order.
"""
new_list = ["g","m","p","a","t"]
print(new_list)
new_list.sort()
print(new_list)


"""
You can have nested list which are just list within list
"""
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]
nested_lists = [list_1,list_2,list_3]
print(nested_lists)


"""
Indexing nested lists
"""

print(nested_lists[0][1])


"""
List comprehensions
"""
first_col = [row[0] for row in nested_lists]
print(first_col)