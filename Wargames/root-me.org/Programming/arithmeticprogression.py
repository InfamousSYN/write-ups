#!/usr/bin/python
import urllib2, urllib
import math, re

def math_func(alpha, sign, beta, u0, n):
	result = u0
	if n == 0:
		return u0
	if sign == "-":
		for i in xrange(1, n+2):
			result = alpha + result - (i-1)*beta
	else:
		for i in xrange(1, n+2):
			result = alpha + result + (i-1)*beta
	
	return result

content = urllib2.build_opener()
content.addheaders = [("User-Agent", "unknown")]
content.addheaders.append(("Cookie", "PHPSESSID=gea27oooj334r5up242r1lbdf3; path=/programmation/ch1/; HttpOnly"))
content.addheaders.append(("Connection", "Keep-Alive"))

response = content.open("http://challenge01.root-me.org/programmation/ch1/", "")
response = response.read()

regex = r"U<sub>n\+1</sub> = \[ (.*) \+ U<sub>n</sub> ] (.) \[ n \* (.*) ]<br />\nU<sub>0</sub> = (.*)\n<br /> Trouver le terme n&deg;(.*) de cette suite."
match = re.search(regex, response)
alpha = int(match.group(1))
sign = match.group(2)
beta = int(match.group(3))
u0 = int(match.group(4))
n = int(match.group(5))

result = math_func(alpha, sign, beta, u0, n)

response = content.open("http://challenge01.root-me.org/programmation/ch1/ep1_v.php?resultat=" + str(result), "")
print(response.read())
