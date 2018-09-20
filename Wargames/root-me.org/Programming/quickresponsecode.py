#!/usr/bin/python
import urllib2, urllib
import re, base64, subprocess

content = urllib2.build_opener()
content.addheaders = [("User-Agent", "unknown")]
content.addheaders.append(("Cookie", "PHPSESSID=kd691dkk2hece70eqkg887bpo2; path=/programmation/ch7/; HttpOnly"))
content.addheaders.append(("Connections", "Keep-Alive"))

response = content.open("http://challenge01.root-me.org/programmation/ch7/").read()

# Download the QR code and write to file locally
regex = r'<img src="data:image/png;base64,(.*)" /><br/>'
result = re.search(regex, response)
result = result.group(1)
result = base64.b64decode(result)
f = open("image-qrc-broken.png", "wb")
f.write(result)
f.close()

# Fixes broken QR image by overlaying the downloaded QR image
# with missing required position patterns
subprocess.Popen("composite blank3.png image-qrc-broken.png image-qrc-fixed.png", stdout=subprocess.PIPE, shell=True).stdout.read()

# Upload QR image to http://zxing.org/w/decode.jspx
result = subprocess.Popen("curl -F 'filename=@image-qrc-fixed.png' http://zxing.org/w/decode", stdout=subprocess.PIPE, shell=True).stdout.r$
regex = r"<pre>The key is (.*)</pre>"
result = re.search(regex, result)
result = result.group(1)

# Upload answer to root-me.org
values = {"metu":result}
post_data = urllib.urlencode(values)
response = content.open("http://challenge01.root-me.org/programmation/ch7/", post_data).read()

print(response)
