try:
  print(2+'hello')
except:
  print("There was a type error")
finally:
  print("Finally this was printed")

try:
  f = open('test (Lecture 61 Exception Handling try, except, finally).txt', 'r')
  f.write('This is a test write')
except:
  print("Error in writing to the file!")
else:
  print("The file was written successfully")

try:
  f = open('test (Lecture 61 Exception Handling try, except, finally).txt', 'r')
  f.write('This is a test write')
except:
  print("There was an error")
finally:
  print("This line of code will always be run")

def askint():
  while True:
    try:
      val = int(input("Please enter an integer: "))
    except:
      print("Looks like you did not enter an integer!")
      continue
    else:
      print("That was an integer")
      break
    finally:
      print("Finally block of code run")
    print(val)
askint()
