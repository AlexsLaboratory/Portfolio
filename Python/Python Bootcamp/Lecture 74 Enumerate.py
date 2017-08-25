l = ['a', 'b', 'c']
for count, item in enumerate(l):
  print(item, count)

for count, item in enumerate(l):
  if count >= 2:
    break
  else:
    print(item)
