# compute gross pay
try:
  h = raw_input('Enter Hours: ')
  hours = float(h)
  r = raw_input('Enter Rate: ')
  rate = float(r)
except:
  print('Error, please enter numeric input.')
  quit()
if hours <= 40:
  pay = hours * rate
else:
  pay = rate * 40 + (rate * 1.5 * (hours - 40))
print('Pay: ' + str(pay))
