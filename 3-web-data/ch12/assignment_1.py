import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# get span tags
spans = soup('span')

count = 0
sum = 0

for span in spans:
  #print span.contents[0]
  count = count + 1
  sum = sum + int(span.contents[0])
  
print 'Count', count
print 'Sum', sum
  