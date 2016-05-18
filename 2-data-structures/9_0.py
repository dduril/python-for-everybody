# Dictionaries

fruits = dict()
fruits['ap'] = 'apple'
fruits['ba'] = 'banana'
fruits['ch'] = 'cherry'
fruits['ki'] = 'kiwi'
fruits['or'] = 'orange'
print fruits
print fruits['ap']
print fruits['ba']
print fruits['ch']
print fruits['ki']
print fruits['or']
print len(fruits)


# Compare list with dictionary
# list
lst = list()
lst.append(21)
lst.append(183)
print lst
lst[0] = 23
print lst
# dictionary
dt = dict()
dt['age'] = 21
dt['course'] = 183
print dt
dt['age'] = 23
print dt

# Dictionary example
word = 'Brontosaurus'
d = dict()
for c in word:
  if c not in d:
    d[c] = 1
  else:
    d[c] = d[c] + 1
print d

# Count names in dictionary
counts = dict()
names = ['Bob', 'Jane', 'Bob', 'John', 'Mary', 'Bob', 'Bob', 'Jane', 'Dave', 'Jenny']
for name in names:
  if name not in counts:
    counts[name] = 1
  else:
    counts[name] = counts[name] + 1
print counts

# Count names using get()
counts = dict()
names = ['Bob', 'Jane', 'Bob', 'John', 'Mary', 'Bob', 'Bob', 'Jane', 'Dave', 'Jenny']
for name in names:
  counts[name] = counts.get(name, 0) + 1
print counts

# Find the most common word
counts = dict()
print 'Enter a line of text:'
line = raw_input('')

words = line.split()
print 'Words:', words

print 'Counting...'
for word in words:
  counts[word] = counts.get(word, 0) + 1

  print 'Counts:', counts

# Loops and dictionaries
counts = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
  print key, counts[key]

# Retrieving lists of keys and values
n = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
print list(n)
print n.keys()
print n.values()
print n.items()

# Example counting most common word
name = raw_input('Enter file: ')
handle = open(name, 'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
  counts[word] = counts.get(word, 0) + 1
  
bigcount = None
bigword = None
for word, count in counts.items():
  if bigcount is None or count > bigcount:
    bigword = word
    bigcount = count
    
print bigword, bigcount









