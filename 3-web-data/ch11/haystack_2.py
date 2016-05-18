import re

hand = open('regex_sum_208442.txt')
numlist = list()
for line in hand:
  line = line.rstrip()
  stuff = re.findall('[0-9]+', line)
  
  if len(stuff) == 0: continue
  
  # debug ------------
  #print stuff
  
  for num in stuff:
    num = int(num)
    numlist.append(num)
  
print 'Sum:', sum(numlist)
