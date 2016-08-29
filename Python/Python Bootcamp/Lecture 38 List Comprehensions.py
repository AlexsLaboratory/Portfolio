l = []
for letter in 'word':
	l.append(letter)
print(l)


"""
List comprehensions
"""
l = [letter for letter in 'word']
print(l)

l = [x**2 for x in range(0,11)]
print(l)

l = [number for number in range(0,11) if number % 2 == 0]
print(l)


"""
Convert Celsius to Fahrenheit
"""
celsius = [0,10,20,1,34.5]
fahrenheit = [(temp * (9/5) + 32) for temp in celsius]
print(fahrenheit)


"""
Nested list comprehensions
"""
l = [x**2 for x in [x**2 for x in range(0,11)]]
print(l)