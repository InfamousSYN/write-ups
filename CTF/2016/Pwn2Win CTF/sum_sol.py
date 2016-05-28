#!/usr/bin/python
import socket
import ssl

def recvData(i):
	data = ""
	result = 0
	data = list(i.recv(1024))
	#print(data)
	data = filter(lambda a: a != ' ', data)
	data = filter(lambda a: a != '\n', data)
	
	for d in data:
		result = int(result) + int(d)
		result = str(result) + '\n'

	return result

def sendData(data):
	i.send(data)

	result = ""
	data = ""
	c = 1
	while 1:
		result = i.recv(1)
		if not result:
			break
		else:
			data += result
			c += 1
	print (data)
	
	return data

# openssl s_client -connect programming.pwn2win.party:9000
if __name__ == '__main__':
	host = "programming.pwn2win.party"
	port = 9000
	result = 0
	data = ""
	count = 0
	max_count = 19

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	i = ssl.wrap_socket(s)

	while (count <= max_count):
		data = recvData(i)
		print("Sending value: %s" % data)
		i.send(data)
		count += 1

	data = sendData(data)
	data = ''.join(data)
	print(data)

'''
openssl s_client -connect programming.pwn2win.party:9000
CONNECTED(00000003)
depth=1 C = US, O = Let's Encrypt, CN = Let's Encrypt Authority X1
verify error:num=20:unable to get local issuer certificate
verify return:0
---
Certificate chain
 0 s:/CN=programming.pwn2win.party
   i:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X1
 1 s:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X1
   i:/O=Digital Signature Trust Co./CN=DST Root CA X3
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIFFjCCA/6gAwIBAgISAajDI9WShwbfVH1PNL3+H4qPMA0GCSqGSIb3DQEBCwUA
MEoxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQD
ExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMTAeFw0xNjAzMTgwMDI2MDBaFw0x
NjA2MTYwMDI2MDBaMCQxIjAgBgNVBAMTGXByb2dyYW1taW5nLnB3bjJ3aW4ucGFy
dHkwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC+SgEaiywKL4VNhRfd
ObMzifb2ilqQeL+Rv3TkEDs9iyKZxpj0lR/TlZfjUv2fXl3eZeMqUchyTb6CoAGT
pCe7xq8BIFeS73s4bR0U8SP6sHNZ5VheGbY7DVIGCxHkJRhB+3DDwW6MB+ktnS0f
BM/3rRpBX4LedheupCqLN498XhdTilzB8SbLzUyXzdaCQzDCHK0ed7TF8fqeZBnt
HEqn2GBPpgHTwyZYhZtDBx9x8XeWsDlBsmXtDbvFNZPSMebANoE40oMofT4L3YrF
ozhQoxxPOiY1I0d6onWoy+SFS+W9UGPjVgU7J8o80UBkR3A/bWWhJumdxI1oyKpw
YSmtAgMBAAGjggIaMIICFjAOBgNVHQ8BAf8EBAMCBaAwHQYDVR0lBBYwFAYIKwYB
BQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFMUiqebG3tFp
ZBuEN6zeJwWyeUPQMB8GA1UdIwQYMBaAFKhKamMEfd265tE5t6ZFZe/zqOyhMHAG
CCsGAQUFBwEBBGQwYjAvBggrBgEFBQcwAYYjaHR0cDovL29jc3AuaW50LXgxLmxl
dHNlbmNyeXB0Lm9yZy8wLwYIKwYBBQUHMAKGI2h0dHA6Ly9jZXJ0LmludC14MS5s
ZXRzZW5jcnlwdC5vcmcvMCQGA1UdEQQdMBuCGXByb2dyYW1taW5nLnB3bjJ3aW4u
cGFydHkwgf4GA1UdIASB9jCB8zAIBgZngQwBAgEwgeYGCysGAQQBgt8TAQEBMIHW
MCYGCCsGAQUFBwIBFhpodHRwOi8vY3BzLmxldHNlbmNyeXB0Lm9yZzCBqwYIKwYB
BQUHAgIwgZ4MgZtUaGlzIENlcnRpZmljYXRlIG1heSBvbmx5IGJlIHJlbGllZCB1
cG9uIGJ5IFJlbHlpbmcgUGFydGllcyBhbmQgb25seSBpbiBhY2NvcmRhbmNlIHdp
dGggdGhlIENlcnRpZmljYXRlIFBvbGljeSBmb3VuZCBhdCBodHRwczovL2xldHNl
bmNyeXB0Lm9yZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAUOfIt/Ru
/ptkMxx/6I49bTwRfLTgZ6DIV/Ac4qCDsrT+LrzHy8WWO+0/xtXxGSkq58xgZ8Lf
4XJ08GZUQLTIrtLExHP3Ajk9Wfz6KXiLdhfeRtp58Cid4P02LQQpdqHANznnIwwo
QoLS4cO7XqfwNtSDHOi3CvUUQEwBA3NF86AYMG4ubMa/PjvlyfcavMt6U7+kDMKP
odGscdopy239iw4ERcWC8YU/MYfWvhxlaKvpjSjabuS5wFA1nvZ90xsg4hCvxCOR
3j5bhYOp2Iwk2XTXr9VM+CyN4nKijegiL+IcU+mK9vJw5YThW4fvZ2NmvDPeVTHu
NeSTq62F6cEYfA==
-----END CERTIFICATE-----
subject=/CN=programming.pwn2win.party
issuer=/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X1
---
No client certificate CA names sent
---
SSL handshake has read 3180 bytes and written 421 bytes
---
New, TLSv1/SSLv3, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 67D6DC082E2EDE503ECB7425E3F91C33E28D76848DB06D7CE950ECF8969445D9
    Session-ID-ctx: 
    Master-Key: 835E985B4832169F43100429AA85722C7DDE58D1ECFCC7FDD84494619BCF61361F1BF6F19820258CDE907B262C49D9BE
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 300 (seconds)
    TLS session ticket:
    0000 - 1d 67 1e 72 b3 b0 ee 50-cb 88 33 03 84 5d 9b 16   .g.r...P..3..]..
    0010 - 06 d0 ac bf 5a 1f af d8-90 04 24 96 e3 b5 52 38   ....Z.....$...R8
    0020 - 81 71 f5 cf 11 6a d9 f8-6a 7e bb 4b 63 2d 7a 79   .q...j..j~.Kc-zy
    0030 - 52 30 9e 2f f1 18 7a f9-c0 29 2e 82 c4 d7 61 bf   R0./..z..)....a.
    0040 - f1 ef 4f b7 21 1c 30 d2-c5 eb b2 fc d8 0c 6e 2e   ..O.!.0.......n.
    0050 - af 14 30 73 0b 5a 05 29-b8 a8 f3 dc b8 fa ac 0e   ..0s.Z.)........
    0060 - c0 47 9f 75 58 ac 88 a7-53 7e 46 23 de cd dc 70   .G.uX...S~F#...p
    0070 - 71 10 8b 9b 13 9c 16 00-f5 16 22 e2 91 56 da 20   q........."..V. 
    0080 - 86 0f 36 1a dc b7 1b e1-cc 67 1d 83 7d 3b 5c 7c   ..6......g..};\|
    0090 - f6 1f 05 64 c3 73 fd c5-a4 88 f1 05 8a a9 62 2e   ...d.s........b.
    00a0 - 0e f6 26 c6 27 ea 89 c7-d7 4e 8e 04 fb 36 14 15   ..&.'....N...6..

    Start Time: 1459063669
    Timeout   : 300 (sec)
    Verify return code: 20 (unable to get local issuer certificate)
---
7 1 8 1 1 9 6 5 8 0
WRONG ANSWER
read:errno=0
'''