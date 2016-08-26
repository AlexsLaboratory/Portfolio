"""
If, Elif, and Else statements
"""

if True:
	print('It was True')
# Output: It was True

if False:
	print('It was True')
# Output:

x = False
if x:
	print('x was True')
else:
	print('I will print when x is anything not True')
# Output: I will print when x is anything not True

x = True
if x:
	print('x was True')
else:
	print('I will print when x is anything not True')
# Output: x was True

loc = 'Bank'
if loc == 'Auto Shop':
	print('Welcome to the Auto Shop!')
elif loc == 'Bank':
	print('Welcome to the bank!')
else:
	print('Where are you?')
# Output: Welcome to the Auto Shop!

loc = 'Auto Shop'
if loc == 'Auto Shop':
	print('Welcome to the Auto Shop!')
elif loc == 'Bank':
	print('Welcome to the bank!')
else:
	print('Where are you?')
# Output: Welcome to the Auto Shop!

loc = 'House'
if loc == 'Auto Shop':
	print('Welcome to the Auto Shop!')
elif loc == 'Bank':
	print('Welcome to the bank!')
else:
	print('Where are you?')
# Output: Where are you?