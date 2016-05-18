import math
import random

# random
for i in range(10):
  x = random.random()
  print x
  
y = random.randint(1, 100)
print y

y = random.randint(1, 100)
print y

a = [1, 2, 3, 4, 5]
b = random.choice(a)
print b

# math
print float(math.pi)

# functions
def repeat_message():
  print_message()
  print_message()
  
def print_message():
  print "Classic first program"
  print "Hello World!"
  
repeat_message() 