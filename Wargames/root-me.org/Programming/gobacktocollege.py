#!/usr/bin/python
import socket
import ssl
import math

host = 'irc.root-me.org'
port = 6697
chan = '#Root-Me_Challenge'
bot = 'Candy'
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
                i.send("PRIVMSG " + bot + " :!ep1\r\n")
                data = i.recv(4096)
                print(data)
        if data.find("PRIVMSG") != -1:
                message = ":".join(data.split(":")[2:])
                message = message[:-1]
                if "/" in message:
                        result = "%0.2f" % (math.sqrt(float(message.split('/')[0]))*float(message.split('/')[1]))
                        i.send('PRIVMSG Candy :!ep1 -rep ' + result + '\r\n')
