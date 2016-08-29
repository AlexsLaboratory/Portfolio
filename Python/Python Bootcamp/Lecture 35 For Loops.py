l = [1,2,3,4,5]
for element in l:
	print(element)

l = [1,2,3,4,5]
for element in l:
	print("Something")


"""
This only prints the event numbers
"""
l = [1,2,3,4,5]
for element in l:
	if element % 2 == 0:
		print(element)
	else:
		print("Odd Number")


"""
This only prints the odd numbers
"""
l = [1,2,3,4,5]
for element in l:
	if element % 2 == 1:
		print(element)
	else:
		print("Even Number")


"""
Adding all of the numbers up in the list
"""
l = [1,2,3,4,5]
tally = 0
for element in l:
	tally += element
print(tally)

s = 'This is a string'
for item in s:
	print(item)


"""
Tuple unpacking
"""
l = [(2,4),(6,8),(10,12)]
for (t1,t2) in l:
	print(t1)


"""
Iterating through a dictionary
"""
d = {'k1':1,'k2':2,'k3':3}
for k,v in d.items():
	print(k,'\n',v)