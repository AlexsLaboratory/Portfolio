"""
Basic while loop
"""
x = 0
while x < 10:
  print('x is currently:',x)
  x += 1
else:
  print('All done')
# Output:
"""
x is currently: 0
x is currently: 1
x is currently: 2
x is currently: 3
x is currently: 4
x is currently: 5
x is currently: 6
x is currently: 7
x is currently: 8
x is currently: 9
All done
"""

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
# Output:
"""
x is currently: 0
x is still less than 10 adding 1 to x
continuing...
x is currently: 1
x is still less than 10 adding 1 to x
continuing...
x is currently: 2
x is still less than 10 adding 1 to x
Hey, x equals 3!
x is currently: 3
x is still less than 10 adding 1 to x
continuing...
x is currently: 4
x is still less than 10 adding 1 to x
continuing...
x is currently: 5
x is still less than 10 adding 1 to x
continuing...
x is currently: 6
x is still less than 10 adding 1 to x
continuing...
x is currently: 7
x is still less than 10 adding 1 to x
continuing...
x is currently: 8
x is still less than 10 adding 1 to x
continuing...
x is currently: 9
x is still less than 10 adding 1 to x
continuing...
"""

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
# Output:
"""
x is currently: 0
x is still less than 10 adding 1 to x
continuing...
x is currently: 1
x is still less than 10 adding 1 to x
continuing...
x is currently: 2
x is still less than 10 adding 1 to x
Hey, x equals 3!
"""
