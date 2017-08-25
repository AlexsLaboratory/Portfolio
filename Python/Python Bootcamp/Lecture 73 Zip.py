from collections import OrderedDict

a = [1, 2, 3]
b = [4, 5, 6]

print(list(zip(a, b)))

x = [1, 2, 3, 4, 5]
y = [2, 2, 10, 1, 1]

for pair in zip(x, y):
  print(max(pair))

print(list(map(lambda pair: max(pair), zip(x, y))))

x1 = [1, 2, 3]
x2 = [4, 5, 6, 7, 8]

print(list(zip(x1, x2)))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

print(list(zip(OrderedDict(d1), d2)))
print(list(zip(OrderedDict(d1), d2.values())))

def switch(d1, d2):
  dout = {}

  for d1key, d2val in zip(OrderedDict(d1), d2.values()):
    dout[d1key] = d2val
  return dout

print(switch(d1, d2))
