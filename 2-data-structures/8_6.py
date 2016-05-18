numlist = list()
while (True):
  inp = raw_input('Enter a number: ')
  if inp == 'done' : break
  value = float(inp)    # assume number, no exception handling
  numlist.append(value)
  
average = sum(numlist) / len(numlist)
print 'Maximum:', max(numlist)
print 'Minimum:', min(numlist)