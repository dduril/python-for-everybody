# Regular Expressions
'''
Quick Guide
^	        Matches the beginning of a line
$	        Matches the end of the line
.	        Matches any character
\s	        Matches whitespace
\S	        Matches any non-whitespace character
*	        Repeats a character zero or more times
*?	        Repeats a character zero or more times (non-greedy)
+	        Repeats a character one or more times
+?	        Repeats a character one or more times (non-greedy)
[aeiou]	    Matches a single character in the listed set
[^XYZ]	    Matches a single character not in the listed set
[a-z0-9]	The set of characters can include a range
(	        Indicates where string extraction is to start
)	        Indicates where string extraction is to end
'''
# Programming language for matching and parsing strings.
# Very powerful and quite cryptic

import re

# using find()
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if line.find('From:') >= 0:
    print line  
print '\n\n'

# using re.search()
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if re.search('From:', line):
    print line 
print '\n\n'
   
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if re.search('^From:', line): # equivalent to line.startswith('From:')
    print line
    
# wild-card characters
#
# ^     match the start of the line
# X     capital X
# .     match any character
# *     any character zero or more times
# :     colon
#
# ^X.*:
hand = open('mbox-short.txt')
for line in hand:
  line = line.rstrip()
  if re.search('^X.*:', line):
    print line
print '\n\n'

# fine-tuning match
#
# ^     match the start of the line
# X     capital X
# -     hyphen
# \S    any non-whitespace character
# +     one or more times
# :     colon
#
# ^X-\S+:

# re.findall()
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print y
y = re.findall('[AEIOU]+', x)
print y
print '\n\n'

# Greedy and Non-Greedy Matching
x = 'From: Using the : character'
y = re.findall('^F.+:', x)  # Greedy - take the larger - 'From: Using the :'
print y
y = re.findall('^F.+?:', x) # Non-Greedy - take the smaller - 'From:'
print y
print '\n\n'

# Sample line from mbox-short.txt
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Get email addresses
y = re.findall('\S+@\S+', x)
print y
print '\n\n'

# Get email addresses only from lines starting with 'From:'
y = re.findall('^From (\S+@\S+)', x)
print y
print '\n\n'

# Get the domain name
lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', lin)
print y
print '\n\n'

# Spam Confidence
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
  line = line.rstrip()
  stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
  if len(stuff) != 1: continue
  num = float(stuff[0])
  numlist.append(num)
  
print 'Maximum:', max(numlist)
print '\n\n'

# Escape Character
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print y
print '\n\n'
















