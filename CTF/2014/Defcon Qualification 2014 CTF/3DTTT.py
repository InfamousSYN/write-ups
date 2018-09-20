#!/usr/bin/python
import socket
import random
import sys

def connector():
	print("Connection being remade!" + "\r\n")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('3dttt_87277cd86e7cc53d2671888c417f62aa.2014.shallweplayaga.me', 1234))
	move(s)

def checker(data, s):
	if 'Must go faster...' in data:
	print("Connection was killed!" + "\n")
	connector()
	if 'You\'ve won -' in data:
		print("Beginning new round!" + "\n")
		connector()
	if 'Play better!' in data:
		print("Beginning new round!" + "\n")
		connector()
	if 'You\'ve won ' in data:
		print("You won!")
		print(data)
		sys.exit(0)

def move(s):
	while 1:
		val1 = random.choice([0,1,2])   # X axis
		val2 = random.choice([0,1,2])   # Y axis
		val3 = random.choice([0,1,2])   # Z axis

		data = s.recv(2000)

		payload = str(val1) + "," + str(val2) + "," + str(val3)
		s.send(payload + "\n")

		checker(data, s)

if __name__=='__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('3dttt_87277cd86e7cc53d2671888c417f62aa.2014.shallweplayaga.me', 1234))
	move(s)
