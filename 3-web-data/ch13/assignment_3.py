import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print '\nRetrieving', url, '\n'
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    place_id = js["results"][0]["place_id"]
    print 'Place id', place_id, '\n'

'''
South Federal University
Academy of Fine Arts Warsaw Poland
'''

'''
C:\Development\Coursera\Python\ch13>assignment_3.py
Enter location: Academy of Fine Arts Warsaw Poland

Retrieving http://python-data.dr-chuck.net/geojson?sensor=false&address=Academy+
of+Fine+Arts+Warsaw+Poland

Retrieved 1949 characters
Place id ChIJAZ-GmmbMHkcR_NPqiCq-8HI

Enter location:
'''