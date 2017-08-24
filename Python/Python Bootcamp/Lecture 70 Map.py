def fahrenheit(c):
  return (9.0/5)*c + 32

def kelvin(c):
  return c + 273.15

tempatures = [0, 22.5, 40, 100, 300, 1000]

print(list(map(fahrenheit, tempatures)))
print(list(map(lambda c: (9.0/5)*c + 32, tempatures)))
print([fahrenheit(x) for x in tempatures])
print(list(map(kelvin, tempatures)))
print(list(map(lambda c: c + 273.15, tempatures)))
print([kelvin(x) for x in tempatures])

a = [1, 2, 3]
b = [4, 5, 6]
c = [9, 8, 9]

print(list(map(lambda z,x,y: x+y+z, a,b,c)))
print(list(map(lambda num: num*-1, a)))
