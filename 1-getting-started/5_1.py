total = 0
count = 0
average = 0
while True:  
  try:
    n = raw_input('Enter a number: ')  
    if n == 'done':
      break
    number = int(n)  
    total = total + number
    count = count + 1
  except:
    print 'Invalid input'    
print total, count, float(total)/float(count) 
  