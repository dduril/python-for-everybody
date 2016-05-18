# Lists

# Create new lists
nums = [10, 20, 30, 40, 50]
fruits = ['apple', 'banana', 'cherry', 'pear', 'strawberry']

# Create a multi-variable nested list
t = [50, 45.8, 'apple', ['red', 'blue', 'green'], [10, 20, 30]]

print nums[0]

# Traversing list
for fruit in fruits:
  print fruit
  
for i in range(len(nums)):
  nums[i] = nums[i] * 2
  print nums[i]
  
# List concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print c

# List slicing
t = [1, 2, 3, 4, 5, 6, 7, 8]
t[1:3]  # 2, 3
t[:4]   # first four elements
t[4:]   # last four elements
t[:]    # all elements

# List methods
# append
t = [1, 2, 3, 4]
t.append(5)
print t

# extend
t1 = [1, 2, 3]
t2 = [4, 5]
t1.extend(t2)
print t1

# sort
t = ['a', 'd', 'e', 'c', 'b']
print t
t.sort()
print t

# pop
t = ['a', 'b', 'c']
x = t.pop(1)
print t
print x

# del
t = ['a', 'b', 'c']
del t[1]
print t

# remove
t = ['a', 'b', 'c']
t.remove('b')
print t

# List functions
nums = [3, 41, 25, 78, 15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)

# Compute the average of a list of numbers
'''
numlist = list()
while (True):
  inp = raw_input('Enter a number: ')
  if inp == 'done' : break
  value = float(inp)    # assume number, no exception handling
  numlist.append(value)
  
average = sum(numlist) / len(numlist)
print 'Average:', average
'''

# Lists and strings

# split letters
s = 'spam'
t = list(s)
print t

# split words
s = 'Star Wars The Force Awakens'
t = s.split()
print t

s = 'Monty-Python-and-the-Holy-Grail'
delimiter = '-'
t = s.split(delimiter)
print t

t = ['Apple', 'Pear', 'Banana', 'Cherry', 'Kiwi']
delimiter = ' '
s = delimiter.join(t)
print s
