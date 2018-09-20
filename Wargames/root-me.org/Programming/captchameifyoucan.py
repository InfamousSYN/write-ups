#!/usr/bin/python
import re, base64, subprocess
import urllib2, urllib

content = urllib2.build_opener()

while 1:
	content.addheaders = [("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0")]
	content.addheaders.append(("Cookie", "PHPSESSID=u6ehp2m5s7tdkasgbbgbb5bnl0; path=/programmation/ch8/; HttpOnly"))
	content.addheaders.append(("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"))
	content.addheaders.append(("Connection", "Keep-Alive"))

	response = content.open("http://challenge01.root-me.org/programmation/ch8/", "")
	response = response.read()

	regex = r'<img src="data:image/png;base64,(.*)" /><br><br>'
	result = re.search(regex, response)
	result = result.group(1)
	result = base64.b64decode(result)

	f = open("image-captcha.png", "w+")
	f.write(result)
	f.close()

	captcha = subprocess.Popen("gocr -i image-captcha.png", stdout=subprocess.PIPE, shell=True).stdout.read()
	captcha = captcha.replace("\n", "")
	captcha = captcha.replace(" ", "")
	captcha = captcha.replace(",", "")
	captcha = captcha.replace("\"", "")

	values = {"cametu":captcha}
	post_data = urllib.urlencode(values)
	content.addheaders.append(("Referer", "http://challenge01.root-me.org/programmation/ch8/?frame=1"))
	response = content.open("http://challenge01.root-me.org/programmation/ch8/", post_data)
	result = response.read()

	if "Congratz" in result:
		print(result)
		break
