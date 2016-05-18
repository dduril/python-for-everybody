def count_letters(word):
  count = 0
  for letter in word:
    if letter == 'a':
      count = count + 1
  return count
  
word = 'banana'
print count_letters(word)
