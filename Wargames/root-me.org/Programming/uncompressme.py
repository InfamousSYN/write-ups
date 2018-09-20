#!/usr/bin/python
import socket
import ssl
import base64
import zlib

host = 'irc.root-me.org'
port = 6697
chan = '#Root-Me_Challenge'
nick = 'syn'
ident = 'syn'
realname = 'syn'
password = [password]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

i = ssl.wrap_socket(s)
i.send("USER %s %s %s :%s\r\n" %(nick, ident, realname, nick))
i.send("NICK %s\r\n" %(nick))

while True:
        data = i.recv(4096)
        print(data)
        if data.find("PING") != -1:
                i.send('PONG ' + data.split()[1] + '\r\n')
        if data.find("001") != -1:
                i.send("join %s\r\n" %(chan))
                i.send("PRIVMSG Candy :!ep4\r\n")
                data = i.recv(4096)
                print(data)
        if data.find("PRIVMSG") != -1:
                encrypted = ":".join(data.split(":")[2:])
                plain = zlib.decompress(base64.b64decode(encrypted))
                i.send("PRIVMSG Candy :!ep4 -rep " + plain + "\r\n")
                print(data)
