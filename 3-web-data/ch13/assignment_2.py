import urllib
import json

url = raw_input('Enter URL: ')
uh = urllib.urlopen(url)
data = uh.read()
print data
print 'Retrieving:',url

info = json.loads(data)

iter = 0
sum = 0

for item in info['comments']:
  print 'Name:', item['name']
  print 'Count:', item['count'] 
  iter = iter + 1
  sum = sum + int(item['count'])
  
print 'Retrieved', len(data),'characters'
print 'Count:', iter  
print 'Sum:', sum
 
'''
Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
Actual data: http://python-data.dr-chuck.net/comments_208448.json (Sum ends with 76)
'''
