## Statements Assessment
Lets test your knowledge


**Use for, split(), and if to create a Statement that will print out words that start with 's'**
```python
st = 'Print only the words that start with s in this sentence'
```
```python
for word in st.split():
	if word[0] == 's':
		print(word)
```

**Use range() to print all the even numbers from 0 to 10.**
```python
print(list(range(0,10,2)))
```

**Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**
```python
l = [num for num in range(1,50) if num%3 == 0]
print(l)
```

**Go through the string below and if the length of a word is even print "even!" and if the length of the word in odd print "odd"!**
```python
st = 'Print every word in this sentence that has an even number of letters'
```
```python
for word in st.split():
	if len(word) % 2 == 0:
		print(word, ": Even")
	else:
		print(word, ": Odd")
```

**Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**
```python
for num in range(1,100):
	if num % 3 == 0 and num % 5 == 0:
		print('FizzBuzz', num)
	elif num % 3 == 0:
		print('Fizz', num)
	elif num % 5 == 0:
		print('Buzz', num)
```

**Use List Comprehension to create a list of the first letters of every word in the string below:**
```python
st = 'Create a list of the first letters of every word in this string'
```
```python
l = [letter[0] for letter in st.split()]
print(l)
```

#### **Great Job!**