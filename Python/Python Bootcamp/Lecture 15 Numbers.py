# Simple addition
print(2+2)

# Simple Multiplication
print(2*2)

# True division is a number that has no decimal
"""
This will chop off any number after the decimal
and will just leave you with a whole number.
"""
print(int(3/2))

# Floating point number also known as a number with a decimal
print(float(3/2))

# Or

print(3/2.0)

# Powers
print(4**5)

# Orders of operations
"""
This is the classic orders of operations that we
have all learned in math where python will read parentheses,
then exponents, then multiplication / division, then addition / subtraction
"""
"""
When run this will do 10*10=100 then do 2+3=5
"""
print(2+10*10+3)
"""
When run this will do 2+10=12 then do 10+3=13 final it will do 12*13=156
"""
print((2+10)*(10+3))

# Simple variables
"""
NOTE: variables can be reassigned a new value
at any point in time in the code
"""

"""
When run a+a should come out to be 10
"""
a = 5
print(a+a)

"""
When run a+a should come out to be 20
"""
a = 10
print(a+a)

"""
You can also use the variable label itself to reassign the variable value
"""

a = 10
a = a+a
print(a)

# Or

a = 10
a += a
print(a)

# Very simple use case for variables

my_income = 100
tax_rate = 0.1
my_taxes = my_income*tax_rate
print(my_taxes)