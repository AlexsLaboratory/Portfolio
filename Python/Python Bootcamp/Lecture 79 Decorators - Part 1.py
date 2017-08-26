def func():
  return 1

print(func())

s = 'This is a global variable'

def func():
  print(locals())

print(globals()['s'])
print(func())

def hello(name='Alex'):
  return 'Hello ' + name

print(hello())

greet = hello
print(greet())

del hello
try:
  print(hello())
except:
  print('An error has occurred')

print(greet())
