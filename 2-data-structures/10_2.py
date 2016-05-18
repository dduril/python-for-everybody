fname = raw_input('Enter file name: ')
try:
  fhand = open(fname)
except:
  print 'File cannot be opened:', fname 
  exit()
  
timestamps = dict()
for line in fhand:
  words = line.split()
  if len(words) == 0 : continue
  if words[0] != 'From' : continue
  # print 'debug:', line.rstrip()
  # print 'debug:', words[5]
  ts = words[5].split(':')
  hours = ts[0]
  timestamps[hours] = timestamps.get(hours, 0) + 1
    
lst = list()
for key, val in timestamps.items():
  lst.append((key, val))
  
lst.sort()

for key, val in lst:
  print key, val
