"""
Normal def function
"""
def square(num):
  return(num**2)
print(square(8))
# Output: 64


"""
Converting def function into a Lambda Expression
"""
square = lambda num: num**2
print(square(10))
# Output: 100

even = lambda num: num % 2 == 0
print(even(8))
# Output: True


"""
The def function below does the same thing as above
"""
def even(num):
  return(num % 2 == 0)
print(even(8))
# Output: True


"""
Grabs the first character of a string
"""
first = lambda s: s[0]
print(first('Hello'))
# Output: H


"""
Reverses the string
"""
rev = lambda s: s[::-1]
print(rev('Hello'))
# Output: olleH


def adder(x,y):
  return(x+y)
print(adder(64,64))
# Output: 128


"""
The Lambda Expression below does the same thing that the def function above does
"""
adder = lambda x,y: x+y
print(adder(64,64))
# Output: 256