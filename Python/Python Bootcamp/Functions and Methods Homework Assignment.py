import string
def vol(radius):
  return (4/3)*(3.14159265359)*radius**3
print(vol(64))

def ran_check(low, num, high):
  if low <= num <= high:
    print("Yes, %s is between %s and %s" %(num, low, high))
  else:
    print("No, %s is not between %s and %s" %(num, low, high ))
ran_check(0,50,100)

def ran_bool(low, num, high):
  if low <= num <= high:
    return True
  else:
    return False
print(ran_bool(0,-1,100))

def up_low(s):
  total_upper = 0
  total_lower = 0
  for case in s:
    if case.islower():
      total_lower += 1
    if case.isupper():
      total_upper += 1
  print("Number of upper case characters: %s"%(total_upper))
  print("Number of lower case characters: %s"%(total_lower))
up_low("Hello Mr. Rogers, how are you this fine Tuesday?")

def unique_list(l):
  return list(set(l))
print(unique_list([1,1,1,1,2,2,2,2,3,3,3,4,5]))

def multiply(numbers):
  total = 1
  for n in numbers:
    total *= n
  print(total)
multiply([1,2,3,-4])

def palindrome(s):
  if s[::-1] == s:
    return True
  else:
    return False
print(palindrome("helleh"))

def ispangram(str1):
  lower_alph = string.ascii_lowercase
  data = str1.lower()
  return set(lower_alph) <= set(data)
print(ispangram("The quick brown fox jumps over the lazy dog"))