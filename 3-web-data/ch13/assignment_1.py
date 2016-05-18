import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')
data = urllib.urlopen(url).read()
print 'Retrieving:',url

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')

iter = 0
sum = 0

for item in lst:
  #print 'Name:', item.find('name').text
  #print 'Count:', item.find('count').text
  #print '\n'
  iter = iter + 1
  sum = sum + int(item.find('count').text)

print 'Retrieved', len(data),'characters'
print 'Count:', iter  
print 'Sum:', sum
  

'''
Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2482)
Actual data: http://python-data.dr-chuck.net/comments_208444.xml (Sum ends with 25)
'''