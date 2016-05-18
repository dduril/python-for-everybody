# ----------------------
# Python for Everybody
# Chapter 6 - Strings
# ----------------------
str1 = "Hello "
str2 = "There"
str3 = str1 + str2
print str3

str4 = '123'
str4 = str4 + 10
# Traceback

x = int(str4) + 10
print x

name = raw_input("Enter: ")
print name

# | b | a | n | a | n | a |
# -------------------------
# | 0 | 1 | 2 | 3 | 4 | 5 |
fruit = 'banana'
letter = fruit[0]
print letter

n = 3
w = fruit[n-1]
print w

zot = 'abc'
print zot[5]
# Traceback

fruit = 'banana'
print fruit, len(fruit)

# indefinite loop
fruit = 'banana'
index = 0
while index < len(fruit):
  letter = fruit[index]
  print index, letter
  index = index + 1
  
# definite loop
fruit = 'banana'
for letter in fruit:
  print letter
  
# Count number of a's in banana
word = 'banana'
count = 0
for letter in word:
  if letter == 'a':
    count = count + 1
print count

# | M | o | n | t | y |   | P | y | t | h | o | n |
# -------------------------------------------------
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11|
s = 'Monty Python'
print s[0:5]    # Monty
print s[6:7]    # P
print s[6:11]   # Python
print s[:2]     # Mo
print s[8:]     # thon
print s[:]      # Monty Python

# String concatentation
a = 'Hello'
b = 'There'
print a + ' ' + b

# in operator
fruit = 'banana'
if 'a' in fruit:
  print 'Found a'
  
name = 'John Smith'
print name.lower()
print name.upper()

# String Methods
stuff = "Hello World"
# Type
print stuff, type(stuff)

# Directory of methods
print dir(stuff)

# Find
pos = fruit.find('na')
print pos

aa = fruit.find('z')
print aa

# Replace
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print nstr

# Whitespace
greet = '     Hello Bob       '
print greet.lstrip()
print greet.rstrip()
print greet.strip()

# Prefixes
line = 'Please have a nice day'
print line.startswith('Please')

# Parsing Strings
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2015'
atpos = data.find('@')
print atpos

sppos = data.find(' ',atpos)
print sppos

host = data[atpos + 1 : sppos]
print host