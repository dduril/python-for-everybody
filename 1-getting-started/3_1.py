# compute gross pay
h = raw_input('Enter Hours: ')
r = raw_input('Enter Rate: ')

hours = float(h)
rate = float(r)

if hours <= 40:
  pay = hours * rate
else:
  pay = rate * 40 + (rate * 1.5 * (hours - 40))

print pay
#print('Pay: ' + str(pay))