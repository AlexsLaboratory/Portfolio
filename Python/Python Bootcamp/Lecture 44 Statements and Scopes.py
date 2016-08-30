"""
Local
"""
f = lambda x: x**2
print(f(4))
# Output: 16

x = 50
def func(x):
	print('x is', x)
	x = 2
	print('Changed local x to', x)
func(x)
print('x is still', x)
# Output: 
"""
x is 50
Changed local x to 2
x is still 50
"""


"""
Enclosing function local
"""
name = 'This is a global name'

def greet():
	# Enclosing function
	name = 'Alex'

	def hello():
		print('Hello', name)
	hello()
greet()
# Output: Hello Alex

print(name)
# Output: This is a global name


"""
Global Statement
"""
x = 50
def func():
	global x
	print('This function is now using the global x!')
	print('Because of global x is:', x)
	x = 2
	print('Ran func(), changed global x to', x)
print('Before calling func(), x is:', x)
func()
print('Value of x (outside of func()) is:', x)
# Output:
"""
Before calling func(), x is: 50
This function is now using the global x!
Because of global x is: 50
Ran func(), changed global x to 2
Value of x (outside of func()) is: 2
"""


