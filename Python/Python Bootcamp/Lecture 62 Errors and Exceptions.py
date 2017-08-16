try:
  for i in ['a', 'b', 'c']:
    print(i**2)
except:
  print("An error occurred!")

try:
  z = 5/0
except:
  print("Can't divide by Zero!")
finally:
  print("All Done!")

def ask():
  while True:
    try:
      n = int(input("Input an integer: "))
    except:
      print("An error occurred! Please try again!")
      continue
    else:
      break
  print(n**2)
ask()
