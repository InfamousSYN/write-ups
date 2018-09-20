#!/usr/bin/python
 
import socket
import struct
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("vortex.labs.overthewire.org" , 5842))
 
b = 0;
 
for i in range(4):
  data = s.recv(4)
  b += struct.unpack("<I", data)[0]
 
s.send(struct.pack("<I",(b & 0xFFFFFFFF)))
 
print s.recv(1024)
s.close ()
