print(bin(1024))
print(hex(1024))

def custom_round(num, up_to):
  num = str(num)
  after_dec = num.split('.')[1]
  before_dec = num.split('.')[0]
  up_to = int(up_to)
  up_to = up_to if up_to != 0 else 1
  if len(after_dec) <= up_to:
    det_num = 0
  else:
    det_num = after_dec[up_to]
  keep = after_dec[:up_to]
  check_int = after_dec[0]
  if int(det_num) < 5:
    dec = str(before_dec + "." + keep)
  else:
    if int(check_int) == 9 and up_to == 1:
      dec = str(int(before_dec) + 1) + "." + str(0)
    else:
      dec = str(before_dec) + "." + str(int(keep) + 1)
  return float(dec)

print(custom_round(8.9785, 1))
print(custom_round(8.9785, 2))
print(custom_round(8.9785, 3))
print(custom_round(8.9785, 8))

s = 'hello how are you Alex, are you feeling okay?'
print(s.islower())

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1.difference(set2))
print(set1.union(set2))
print({x:x**3 for x in range(5)})

l = [1,2,3,4]
l.reverse()
print(l)

l = [3,4,2,5,1]
l.sort()
print(l)
