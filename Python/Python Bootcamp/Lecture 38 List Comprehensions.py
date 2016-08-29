l = []
for letter in 'word':
	l.append(letter)
print(l)
# Output: ['w', 'o', 'r', 'd']


"""
List comprehensions
"""
l = [letter for letter in 'word']
print(l)
# Output: ['w', 'o', 'r', 'd']

l = [x**2 for x in range(0,11)]
print(l)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

l = [number for number in range(0,11) if number % 2 == 0]
print(l)
# Output: [0, 2, 4, 6, 8, 10]


"""
Convert Celsius to Fahrenheit
"""
celsius = [0,10,20,1,34.5]
fahrenheit = [(temp * (9/5) + 32) for temp in celsius]
print(fahrenheit)
# Output: [32.0, 50.0, 68.0, 33.8, 94.1]


"""
Nested list comprehensions
"""
l = [x**2 for x in [x**2 for x in range(0,11)]]
print(l)
# Output: [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]