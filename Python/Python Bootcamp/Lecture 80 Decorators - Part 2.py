def hello(name='Alex'):
  def greet():
    return '\t This is inside the greet() function'

  def welcome():
    return '\t THis is inside the welcome() function'

  if name == 'Alex':
    return greet
  else:
    return welcome

x = hello()
print(x)
print(x())
