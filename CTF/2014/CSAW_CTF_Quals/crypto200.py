#!/usr/bin/python
import socket
import re
import sys

host = "54.209.5.48"
port = 12345

def ciphergrabber(data):
	input = ""
	output = ""
	result = ""
	input = data
	if "psifer text:" in input:
		print("[*] Editing received data for string to decrypt.")
		regex = r'psifer text:(.*)'
		result = re.search(regex, input)
		result = result.group(0)
		result = result.replace("psifer text: ", "psifertext:")
		output  = result.split(":")[1]
		print("The ciphertext for this stage is: " + str(output))
		return output
	else:
		print("No psifer text was found!")
		sys.exit(1)

def decrypt1(text):
	key=0
	a = list(text)
	char = a[0]
	tlet = "t"
	xx = ""
	answer = ""
	while (char != tlet):
    key+=1
    char = chr(ord(char) + 1)
	j = 0
	while j < len(text):
    a[j] = chr(ord(a[j]) + key)
    intval = ord(a[j])
    space = ord(a[j]) - key
    if space == 32:
      a[j] = " "
    elif intval > 122:
      intval = intval - 26
      a[j] = chr(intval)
    j+=1
	xx = ''.join(a)
	xx = xx + '\n'
	answer = xx[28:]
	return answer

if __name__ == "__main__":
	print("[*] Connecting to server!")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	# Stage 1
	print(s.recv(1024))
	data1 = s.recv(1024)
	ciphertext1 = ciphergrabber(data1)
	message = decrypt1(ciphertext1)
	s.send(message)
	print("[*] Sending plaintext message now. Message is: " + message)

	# Stage 2
        print("[*] Getting the ciphertext for stage 2.")
	s.recv(1024)
	data2 = s.recv(2014)
	print(data2)
	ciphertext2 = ciphergrabber(data2)


	sys.exit(0)
