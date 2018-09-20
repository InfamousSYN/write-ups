#!/usr/bin/python

I = 5
SOLUCE = [57, 73, 79, 16, 18, 26, 74, 50, 13, 38, 13, 79, 86, 86, 87]
KEY = "I know, you love decrypting Byte Code !" 
PASS = "0"*len(SOLUCE)
KEYOUT = []

for X in range(len(SOLUCE)):
        KEYOUT.append(chr(((SOLUCE[X] ^ ord(KEY[I])) - I) %255))
        I = I + 1 % len(KEY)
print(KEYOUT)
