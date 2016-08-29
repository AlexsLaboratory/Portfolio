l = [1,2,3,4,5]
for element in l:
	print(element)
# Output:
"""
1
2
3
4
5
"""


l = [1,2,3,4,5]
for element in l:
	print("Something")
# Output:
"""
Something
Something
Something
Something
Something
"""


"""
This only prints the even numbers
"""
l = [1,2,3,4,5]
for element in l:
	if element % 2 == 0:
		print(element)
	else:
		print("Odd Number")
# Output:
"""
Odd Number
2
Odd Number
4
Odd Number
"""


"""
This only prints the odd numbers
"""
l = [1,2,3,4,5]
for element in l:
	if element % 2 == 1:
		print(element)
	else:
		print("Even Number")
# Output:
"""
1
Even Number
3
Even Number
5
"""


"""
Adding all of the numbers up in the list
"""
l = [1,2,3,4,5]
tally = 0
for element in l:
	tally += element
print(tally)
# Output: 15

s = 'This is a string'
for item in s:
	print(item)
# Output:
"""
T
h
i
s
 
i
s
 
a
 
s
t
r
i
n
g
"""


"""
Tuple unpacking
"""
l = [(2,4),(6,8),(10,12)]
for (t1,t2) in l:
	print(t1)
# Output:
"""
2
6
10
"""


"""
Iterating through a dictionary
"""
d = {'k1':1,'k2':2,'k3':3}
for k,v in d.items():
	print(k,'\n',v)
# Output:
"""
k1 
 1
k2 
 2
k3 
 3
"""