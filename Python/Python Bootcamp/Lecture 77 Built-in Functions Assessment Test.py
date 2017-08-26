def word_length(phrase):
  return [len(x) for x in phrase.split()]

print(word_length('How long are the words in this phrase'))

def digits_to_num(digits):
  return ''.join([str(x) for x in digits])

print(digits_to_num([3, 4, 3, 2, 1]))

def filter_words(word_list, letter):
  return [x for x in word_list if x[0] == letter]

print(filter_words(['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart'], 'h'))

def concatenate(L1, L2, connector):
  return [L1[x] + connector + L2[x] for x in range(len(L1))]

print(concatenate(['A', 'B'], ['a', 'b'], '-'))

def d_list(L):
  data = {}
  i = 0
  for x in L:
    data[x] = i
    i+=1
  return data

print(d_list(['a', 'b', 'c']))

def count_match_index(L):
  return len([L[x] for x in range(len(L)) if L[x] == x])

print(count_match_index([0, 2, 2, 1, 5, 5, 6, 10]))
