d = {'k1':1,'k2':2}
print({x:x**2 for x in range(16)})

for k in d.keys():
  print(k)

for v in d.values():
  print(v)

for item in d.items():
  print(item)

print(d.items())
print(d.keys())
print(d.values())
