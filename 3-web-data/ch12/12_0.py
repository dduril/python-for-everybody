import re
import socket
import urllib

# using socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
  data = mysock.recv(512)
  if (len(data) < 1 ):
    break
  print data
mysock.close()


print '\n\n'

# using urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
  print line.strip()
  
print '\n\n'

# using urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
counts = dict()
for line in fhand:
  words = line.split()
  for word in words:
    counts[word] = counts.get(word,0) + 1
print counts

print '\n\n'

# parsing HTML using regular expressions
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
  print link
  
print '\n\n'

# parsing HTML with BeautifulSoup
#import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
  print tag.get('href', None)


