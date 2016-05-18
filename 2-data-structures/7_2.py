# Prompt the user for the file name with exception handling
fname = raw_input('Enter the file name: ')
try:
  fhand = open(fname)
except:
  print 'File cannot be opened:', fname
  exit()

count = 0
total = 0
for line in fhand:
  if line.startswith('X-DSPAM-Confidence:'):  
    #print line
    #print type(line)
    line = line.replace('X-DSPAM-Confidence:', '')
    total = total + float(line)
    count = count + 1
print 'Average spam confidence:', total / count