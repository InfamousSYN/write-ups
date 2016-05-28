#!/usr/bin/python
import socket

plist = [9999, 8888, 7777, 6666, 5555, 4444, 3333, 2222, 1111, 54321]
host = '52.64.111.123'
data = ""

for p in plist:
	print("Attempting to connect to %s on port %s" % (host, p))
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1.0)
		s.connect((host, p))

		data += s.recv(1024)
		data += s.recv(1024)
		data += s.recv(1024)

		s.close()

	except Exception as e:
		continue

print data

'''
% python sheldon-sol.py              
Attempting to connect to 52.64.111.123 on port 9999
Attempting to connect to 52.64.111.123 on port 8888
Attempting to connect to 52.64.111.123 on port 7777
Attempting to connect to 52.64.111.123 on port 6666
Attempting to connect to 52.64.111.123 on port 5555
Attempting to connect to 52.64.111.123 on port 4444
Attempting to connect to 52.64.111.123 on port 3333
Attempting to connect to 52.64.111.123 on port 2222
Attempting to connect to 52.64.111.123 on port 1111
Attempting to connect to 52.64.111.123 on port 54321


flag{Knock_Knock_Knock_Penny}

'''