fname = raw_input('Enter file name: ')
try:
  fhand = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()
  
addresses = list()
counts = dict()
for line in fhand:
  words = line.split()
  if len(words) == 0 : continue
  if words[0] != 'From' : continue
  addresses.append(words[1])

for address in addresses:
  counts[address] = counts.get(address, 0) + 1
print counts