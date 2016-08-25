# Answer the following questions:
## Test your knowledge.

**Answer the following questions**

Write a brief description of all the following Object Types and Data Structures we've learned about:

1. Numbers: A date type to store numeric values. They are immutable data types.

2. Strings: One of the most basic ways to store text in Python 3X or Python 2X as a "string of bytes". Strings can also be used to store binary data.

3. Lists: It is a way to sort a sequence of values.

4. Tuples: It is an immutable ordered sequence of values.

5. Dictionaries: It is composed of arbitrary keys and values which can sometimes be called a "hash map" in other languages. A dictionary much resembles a list.

## Numbers:

Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25

**Multiplication:**
```python
print(25.0625*4)

```
**Division:**
```python
print(401/4)
```
**An exponent:**
```python
print(25.0625**1.43035)
```
**Addition:**
```python
print(50+50+.25)
```
**Subtraction:**
```python
print(512-411.75)
```

Explain what the cell below will produce and why. Can you change it so the answer is correct?

```python
print(3/2)
```

**Python3:**
* In python3 the equation above will equal 1.5 because of the division behavior.

**Python:**
* In python the equation above will equal 1 because of the division behavior. To make it print out 1.5 you have to run...

```python
print(3/2.0)

# Or

print(float(3)/2)
```

Answer these 3 questions without typing code. Then type code to check your answer.

* What is the value of the expression 4 * (6 + 5)
	```text
	44
	```

* What is the value of the expression 4 * 6 + 5
	```text
	29
	```

* What is the value of the expression 4 + 6 * 5
	```text
	34
	```
 
What is the *type* of the result of the expression 3 + 1.5 + 4?

* The type of the expression above is a float.


What would you use to find a number’s square root, as well as its square?

**Square root:**
```python
print(256 ** 0.5)
```

**Square:**
```python
print(16 ** 2)
``` 
## Strings:

Given the string 'hello' give an index command that returns 'e'. Use the code below:
```python
s = 'hello'
print(s[1])
```

Reverse the string 'hello' using indexing:
```python
s = 'hello'
print(s[::-1])
```

Given the string hello, give two methods of producing the letter 'o' using indexing.

```python
s = 'hello'
# 1st
print(s[4])

# 2nd
print(s[-1])
```

## Lists:

Build this list [0,0,0] two separate ways.

```python
# 1st
l = [0,0,0]
print(l)

# 2nd
l = [0]*3
print(l)
```
 
Reassign 'hello' in this nested list to say 'goodbye' item in this list:

```python
l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'
print(l)
```
Sort the list below:

```python
l = [4,5,8,2,10]
print(l.sort())
```

## Dictionaries:

Using keys and indexing, grab the 'hello' from the following dictionaries:

```python
d = {'simple_key':'hello'}
print(d['simple_key'])
```

```python
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])
```

```python
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])
```

```python
d = {'k1':[1,2,{'k2':['this is tricky',{'toughie':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['toughie'][2][0])
```

Can you sort a dictionary? Why or why not?

* They cannot be sorted because they are absolutely orderless.

## Tuples:

What is the major difference between tuples and lists?

* The major difference between tuple and lists is that tuples are immutable which means that they cannot be modified once they are created. A list is a sequence which is mutable. It can be modified after it is created, and it supports supplementary operations too.

How do you create a tuple?
```python
t = ('biology','chemistry','physics')
print(t)
```

## Sets:

What is unique about a set?

* Everything in a set has to be unique. If it is not it will remove all of the duplicates of that item.

Use a set to find the unique values of the list below:

```python
l = [1,2,2,33,4,4,11,22,3,3,2]
print(set(l))
```

## Booleans:

For the following quiz questions, we will get a preview of comparison operators:

| Operator | Description | Example |
| -------- | ----------- | ------- |
| == | If the values of two operands are equal, then the condition becomes true. | (a == b) is not true. |
| != | If values of two operands are not equal, then condition becomes true. | 
| <> | If values of two operands are not equal, then condition becomes true. | (a <> b) is true. This is similar to != operator. |
| > | If the value of left operand is greater than the value of right operand, then condition becomes true. | (a > b) is not true. |
| < | If the value of left operand is less than the value of right operand, then condition becomes true. | (a < b) is true. |
| >= | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. | (a >= b) is not true. |
| <= | If the value of left operand is less than or equal to the value of right operand, then condition becomes true. | (a <= b) is true. |

What will be the resulting Boolean of the following pieces of code.
```python
print(2 > 3)
```
**Output:** `False`

```python
print(3 <= 2)
```
**Output:** `False`

```python
print(3 == 2.0)
```
**Output:** `False`

```python
print(3.0 == 3)
```
**Output:** `True`

```python
print(4**0.5 != 2)
```
**Output:** `False`

Final Question: What is the boolean output of the cell block below?

```python
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

l_one[2][0] >= l_two[2]['k1']
```
**Output:** `False`