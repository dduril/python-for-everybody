data = 'X-DSPAM-Confidence: 0.8475'
spos = data.find(':')
print spos

epos = len(data)
print epos

extract = float(data[spos + 1 : epos].lstrip())
print extract
#print type(extract)


# solution
'''
x = 'X-DSPAM-Confidence: 0.8475'
print x

pos = x.find[:]
print pos
print x[pos+1:]
num = float(x[pos+1:])
print num, type(num)
'''