def even_check(num):
  if num % 2 == 0:
    return True
  else:
    return False

nums = range(10)
print(list(filter(even_check, nums)))
print(list(filter(lambda num: num % 2 == 0, nums)))
print(list(filter(lambda num: num > 3, nums)))
