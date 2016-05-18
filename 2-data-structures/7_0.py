# File IO

# File handle
fhand = open('mbox.txt')
print fhand


# Newline example
stuff = "Hello\nWorld"
print stuff


# Newline example
str = "X\nY"
print str
print len(str)


# Print each line in a file
fhand = open('mbox.txt')
for line in fhand:
    print line

    
# Count lines in file
fhand = open('mbox.txt')
count = 0
for line in fhand:
  count = count + 1
print "Line count:", count


# Lines that start with from
fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if not line.startswith('From:'):
    continue
  print line

  
# Search for lines containing string
fhand = open('mbox-short.txt')
for line in fhand:
  line = line.rstrip()
  if line.find('@uct.ac.za') == -1:
    continue
  print line

  
# Prompt the user for the file name
fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
print 'There were', count, 'subject lines in', fname


# Prompt the user for the file name with exception handling
fname = raw_input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()
count = 0
for line in fhand:
  if line.startswith('Subject:'):
    count = count + 1
print 'There were', count, 'subject lines in', fname


# Open file in write mode
fout = open('output.txt', 'w')
print fout


# Writing to a file
line1 = 'Adding some information to the file'
fout.write(line1)
fout.close()


















