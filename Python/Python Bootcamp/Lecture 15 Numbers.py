"""
Just your basic addition.
"""
print(8+8)
# Output: 16


"""
Just your basic multiplication.
"""
print(8*8)
#  Output: 64


"""
This will chop off any number after the decimal
and will just leave you with a whole number.

NOTE: True division is a number that has no decimal point.
"""
print(int(8/2.9))
# Output: 4


"""
Floating point number also known as a number with a decimal point.
"""
print(float(8/2.5))
# Output: 3.2

# Or

print(8/2.5)
# Output: 3.2


"""
Powers
"""
print(8**2)
# Output: 64


"""
When run, it will do 10*10=100 then it will do 2+3=5.

NOTE: This is the classic orders of operations that we
have all learned in math. Python will read parentheses,
then exponents, then multiplication / division, then addition / subtraction.
"""
print(2+10*10+3)
# Output: 105


"""
When run, it will do 2+10=12 then do 10+3=13 finally it will do 12*13=156.

NOTE: It does this because we specified a custom order with the parentheses.
"""
print((2+10)*(10+3))
# Output: 156


"""
When run, it will do "a+a".
"""
a = 5
print(a+a)
# Output: 10


"""
When run, it will do "a+a".

NOTE: Variables can be reassigned a new value
at any point in time in the code.
"""
a = 10
print(a+a)
# Output: 20


"""
You can also use the variable labels them self to reassign the variable value.
"""
b = 10
c = b+b
print(c)
# Output: 20

# Or

b = 10
c += b
print(b)
# Output: 20


"""
Very simple use case for variables.
"""
my_income = 108
tax_rate = 0.1
my_taxes = my_income*tax_rate
print(my_taxes)
# Output: 10.8