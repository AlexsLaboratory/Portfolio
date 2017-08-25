from functools import reduce
nums = [47, 11, 42, 48, 534, 13, 32, 62]
max_find = lambda a, b: a if a > b else b
print(reduce(max_find, nums))

def max_num(l):
  largest = l[0]
  for x in l:
    if x > largest:
      largest = x
  return largest
print(max_num(nums))
