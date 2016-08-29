# """
# Basic while loop
# """
# x = 0
# while x < 10:
# 	print('x is currently:',x)
# 	x += 1
# else:
# 	print('All done')


"""
Break, Continue, Pass
"""
# Continue
x = 0
while x < 10:
	print('x is currently:',x)
	print('x is still less than 10 adding 1 to x')
	x += 1
	if x == 3:
		print('Hey, x equals 3!')
	else:
		print('continuing...')
		continue
		
# Break
x = 0
while x < 10:
	print('x is currently:',x)
	print('x is still less than 10 adding 1 to x')
	x += 1
	if x == 3:
		print('Hey, x equals 3!')
		break
	else:
		print('continuing...')