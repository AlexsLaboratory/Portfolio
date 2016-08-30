"""
Creating our own functions
"""

def say_hello(name):
	print('Hello', name)
say_hello("Alex")
# Output: Hello Alex

def addition(num1,num2):
	return(num1 + num2)
print(addition(4,4))
# Output: 8

def is_prime(num):
	'''
	This will check for prime numbers
	'''
	for n in range(2,num):
		if num % n == 0:
			print(num, 'is not a prime number')
			break
	else:
		print(num, 'is a prime number')

is_prime(12)
# Output: 12 is not a prime number
is_prime(13)
# Output: 13 is a prime number