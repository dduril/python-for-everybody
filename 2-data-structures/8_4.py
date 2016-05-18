fhand = open('romeo.txt')
words = []
for line in fhand:
  line = line.rstrip()
  print line
  
  s = line.split()
  print s
  
  for w in s:
    if w in words:
      continue
    else:
      words.append(w)

  
print '\n'
words.sort()
print words