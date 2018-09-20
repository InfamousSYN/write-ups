#!/usr/bin/python
import socket
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("semtex.labs.overthewire.org", 24000))

data = s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
data += s.recv(6000)
#print("The data received is: " + str(binascii.hexlify(data)))

x = binascii.hexlify(data)
data2 = [x[i] + x[i+1] for i in range(0,len(x),2)]                              # Grouping every 2 elements together.
data3 = map(lambda i: data2[i], filter(lambda i: i%2 == 0, range(len(data2))))  # Deletes every old element from the list.
data4 = ''.join(data3)                                                          # Turns the list back into a string.
data5 = binascii.unhexlify(data4)
with open('out.bin', 'wb') as f:
        f.write(data5)
f.close()
s.close()
