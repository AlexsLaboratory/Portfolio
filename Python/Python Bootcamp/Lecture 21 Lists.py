"""
Lists can hold any object type such as integers, floating points and strings.
"""
list_one = ["one", "two", "three", 4, 4.5]
print(list_one)
# Output: ['one', 'two', 'three', 4, 4.5]


"""
The "len" function also works with lists and will count how many elements there are in the list.
"""
list_two = ["one", "two", "three", 4, 4.5]
print(len(list_two))
# Output: 5


"""
Prints the first element in the list.
"""
list_three = ["one", "two", "three", 4, 4.5]
print(list_three[0])
# Output: one


"""
Prints everything from the second element in the list onward.
"""
list_four = ["one", "two", "three", 4, 4.5]
print(list_four[1:])
# Output: ['two', 'three', 4, 4.5]


"""
Prints everything from the beginning of the list up to the second element in the list.
"""
list_five = ["one", "two", "three", 4, 4.5]
print(list_five[:2])
# Output: ['one', 'two']


"""
Prints each element in the list in reverse order.
"""
list_six = ["one", "two", "three", 4, 4.5]
print(list_six[::-1])
# Output: [4.5, 4, 'three', 'two', 'one']


"""
Concatenate lists with other lists.

NOTE: This does not change either of the variables.
"""
print(my_list + my_list2)
# Output: ['one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5]


"""
Permanently add one list to another list.

NOTE: This does change the variables.
"""
con_list = list_one + list_two
print(con_list)
# Output: ['one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5]


"""
Multiply list too. This will print your list 8 times and make it one list.
"""
print(list_one * 8)
# Output: ['one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5, 'one', 'two', 'three', 4, 4.5]


"""
Append attributes onto the end of lists.
"""
list_seven = ["one", "two", "three", 4, 4.5]
print(list_seven)
list_seven.append("I am appended")
print(list_seven)
# Output: ['one', 'two', 'three', 4, 4.5, 'I am appended']


"""
Pop which will "pop" off element "0".

NOTE: if you do not specify a pop off index location it will by default pop off the last element in the list.
"""
list_eight = ["one", "two", "three", 4, 4.5]
print(list_eight.pop(0))
print(list_eight)
# Output: ['two', 'three', 4, 4.5]


"""
Reverse the order of a list with the reverse function.
"""
list_nine = ["g", "m", "p", "a", "t"]
print(list_nine)
list_nine.reverse()
print(list_nine)
# Output: ['t', 'a', 'p', 'm', 'g']


"""
Sort the order of a list.

NOTE: It will sort numbers by ascending order and will sort letters by alphabetical order.
NOTE: It will not sort letters and numbers that are in the same list.
"""
# Letters
list_ten = ["g", "m", "p", "a", "t"]
print(list_ten)
list_ten.sort()
print(list_ten)
# Output: ['a', 'g', 'm', 'p', 't']

# Numbers
list_eleven = [10, 1889, 594925, 9, 184]
print(list_eleven)
list_eleven.sort()
print(list_eleven)
# Output: [9, 10, 184, 1889, 594925]


"""
You can have nested list which are just list within list.
"""
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]
nested_lists = [list_1,list_2,list_3]
print(nested_lists)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


"""
Indexing nested lists.
"""
print(nested_lists[0][1])
# Output: 2


"""
List comprehensions.
"""
first_col = [row[0] for row in nested_lists]
print(first_col)
# Output:[1, 4, 7]