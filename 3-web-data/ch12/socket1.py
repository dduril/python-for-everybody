import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()

'''
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\Doug>cd ../../development/coursera/python/ch12

C:\Development\Coursera\Python\ch12>dir
 Volume in drive C is OS
 Volume Serial Number is FA53-81CE

 Directory of C:\Development\Coursera\Python\ch12

12/16/2015  08:30 PM    <DIR>          .
12/16/2015  08:30 PM    <DIR>          ..
12/16/2015  05:53 PM             1,248 12_0.py
12/11/2015  09:03 AM            79,378 BeautifulSoup.py
12/16/2015  06:00 PM            69,507 BeautifulSoup.pyc
12/16/2015  08:30 PM               318 socket1.py
12/16/2015  05:57 PM               252 soup.py
               5 File(s)        150,703 bytes
               2 Dir(s)  1,235,957,645,312 bytes free

C:\Development\Coursera\Python\ch12>socket1.py
HTTP/1.1 200 OK
Date: Thu, 17 Dec 2015 04:31:44 GMT
Server: Apache
Last-Modified: Mon, 12 Oct 2015 14:55:29 GMT
ETag: "20f7401b-1d3-521e9853a392b"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=604800, public
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: origin, x-requested-with, content-type
Access-Control-Allow-Methods: GET
Connection: close
Content-Type: text/plain

Why should you learn to write programs?

Writing programs (or programming) is a very creative

and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.  This book assumes that
everyone needs to know how to program, and that once
you know how to program you will figure out what you want
to do with your newfound skills.


C:\Development\Coursera\Python\ch12>
'''