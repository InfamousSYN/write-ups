#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import httplib2, urllib
import re

def recvData(s):
	result = ""
	data = ""
	i = 0
	
	while 1:
		result = s.recv(1)
		if '\n' in result:
			break
		else:
			data += result
			i += 1
	return data.split(" ")

def mapLookup(result):
	h = httplib2.Http()
	host = "https://maps.googleapis.com/maps/api/geocode/json?"
	
	location = result[0] + ", " + result[1]
	query = urllib.urlencode({"latlng":location})
	resp, content = h.request(host + query, method="GET")
	print("[-] Looking up received geocode for: %s" % location)

	# gets location
	regex = r'^.*?"locality"'
	resultLoc = re.findall(regex, content, re.DOTALL)[0]
	regex = r'"long_name" : (.*?),'
	resultLoc = re.findall(regex, resultLoc)[-1].strip("\"")

	return resultLoc

if __name__ == '__main__':
	host = 'exploit1.ctf.shearwater.com.au'
	port = 31438

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	while 1:
		result = recvData(s)
		print(result)
		result = mapLookup(result)
		if (result == 'Città del Vaticano'):
			result = 'Vatican City'
		elif (result == 'München'):
			result = 'Munich'
		elif (result == 'Cando'):
			result = 'Maza'
		elif (result == 'Shinjuku-ku'):
			result = 'Tokyo'
		elif (result == 'Ciudad de México'):
			result = 'Mexico City'
		elif (result == 'São Paulo'):
			result = 'Sao Paulo'
		elif(result == 'L-Imġarr'):
			result = 'Mgarr'
		print("Sending: %s\n" % result)
		s.send(result)
	s.close()
