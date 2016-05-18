# Tuples
# Are immutable - you cannot alter its contents
# String tuple
x = ('John', 'Julie', 'Glenn')
print x[2]

# Integer tuple
y = (5, 25, 45)
print y
print max(y)
for iter in y:
  print y

# Lists - are mutable
x = [4, 9, 21]
x[2] = 15
print x

x = (3, 2, 1)
x.sort()        # Can't do - would alter tuple
x.append(5)     # Can't do
x.reverse()     # Can't do

# Check what you can do with a list or tuple
lst = list()
dir(lst)

tpl = tuple()
dir(tpl)

# Tuples and assignments
(x, y) = (4, 'fred')
print y
a, b = (99, 98)    # Can omit the parenthesis
print a

# Tuples and dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
  print k, v
  
tups = d.items()
print tups

# Tuples are comparable
(0,1,2) < (5,1,2)                       # True
('Jones', 'Sally') > ('Adams', 'Sam')   # True

# Sorting lists of tuples
d = {'a':10, 'b':1, 'c':22}
t = d.items()
print t
t.sort()
print t

# Using sorted()
d = {'a':10, 'b':1, 'c':22}
t = d.items()
t = sorted(d.items())
print t

for k,v in sorted(d.items()):
  print k,v

# Sort by values instead of key
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
  tmp.append((v,k))
  
print tmp
tmp.sort(reverse=True)
print tmp

# Find the 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word, 0) + 1
    
lst = list()
for key, val in counts.items():
  lst.append((val,key))
  
lst.sort(reverse=True)

for val, key in lst[:10]:
  print key, val
  
# Shorter version - list comprehension
c = {'a':10, 'b':1, 'c':22}
print sorted( [ (v,k) for k,v in c.items() ] )

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  





























