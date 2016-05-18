maximum = None
minimum = None
while True:  
  try:
    n = raw_input('Enter a number: ') 
    
    if n == 'done':
      break
      
    number = int(n)
    
    if minimum is None:
      minimum = number
    elif number < minimum:
      minimum = number
      
    if maximum is None:
      maximum = number
    elif number > maximum:
      maximum = number
      
  except:
    print 'Invalid input' 
    
print maximum, minimum