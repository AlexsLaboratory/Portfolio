## Functions and Methods Homework
Complete the following questions:

**Write a function the computes the volume of a sphere given its radius.**
```python
def vol(rad):
	v = (4)*(3.14159265)*(rad**3) / 3
	return(v)
print(vol(60))
```

**Write a function that checks whether a number is in a given range (Inclusive of high and low).**
```python
def run_check(num,low,high):
	if num in range(int(low),int(high + 1)):
		return('{x} is within range').format(x = num)
	else:
		return('{x} is not within range').format(x = num)
print(run_check(64,0,100))
```

if you only wanted to return a boolean:
```python
def run_bool(num,low,high):
	if num in range(int(low),int(high + 1)):
		return(True)
	else:
		return(False)
print(run_bool(64,0,100))

# Or

def run_bool(num,low,high):
	return(num in range(int(low),int(high + 1)))
print(run_bool(64,0,100))
```

**Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.**
```text
Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
```
```python
def up_low(s):
	d = {'upper':0, 'lower':0}
	for c in s:
		if c.isupper():
			d['upper']+=1
		elif c.islower():
			d['lower']+=1
		else:
			pass
	print('Original String:', s)
	print('No. of Upper case characters:', d['upper'])
	print('No. of Lower case Characters:', d['lower'])
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
```

**Write a Python function that takes a list and returns a new list with unique elements of the first list.**
```text
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
```
```python
def unique_list(l):
	return(list(set(l)))
print(unique_list([1,1,1,1,2,2,2,7,7,4]))

# Or

def unique_list(l):
	x = []
	for a in l:
		if a not in x:
			x.append(a)
	return(x)
print(unique_list([1,1,1,1,2,2,2,7,7,4]))
```

**Write a Python function to multiply all the numbers in a list.**
```text
Sample List : [1, 2, 3, -4]
Expected Output : -24
```
```python
def multiply(numbers):
	total = 1
	for x in numbers:
		total *= x
	return(total)
print(multiply([1,2,3,-4]))
```

**Write a Python function that checks whether a passed string is palindrome or not.**

**Note:** A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
```python
def palindrom(s):
	s = s.replace(' ', '')
	return(s == s[::-1])
print(palindrom('nurses run'))
```
**Hard:**

Write a Python function to check whether a string is pangram or not.
```text
Note: Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
```
```python
def ispangram(str1):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphaset = set(alphabet)
	if alphaset <= set(str1.lower()):
		return(True)
	else:
		return(False)
print(ispangram('The quick brown fax jumps over the lazy dog'))

# Or

def ispangram(str1):
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphaset = set(alphabet)
	return(alphaset <= set(str1.lower()))
print(ispangram('The quick brown fax jumps over the lazy dog'))
```

**Great Job!**