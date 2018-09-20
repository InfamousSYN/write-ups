#!/usr/bin/python

# $ file ch19.pyc 
# ch19.pyc: python 3.1 byte-compiled
# disassembled with unwind - https://github.com/evanw/unwind
# rebuilt for python2.7 - input() was replaced for raw_input()

if __name__ == '__main__':
        print("Welcome to the RootMe python crackme")
        PASS = raw_input("Enter the Flag: ")

        KEY = ("I know, you love decrypting Byte Code !")
        SOLUCE = [57, 73, 79, 16, 18, 26, 74, 50, 13, 38, 13, 79, 86, 86, 87]
        KEYOUT = []
        I = 5

        for X in PASS:
                KEYOUT.append(ord(X) + I ^ ord(KEY[I]) % 255)
                I = I + 1 % len(KEY)
        if SOLUCE == KEYOUT:
                print("You Win")
        else:
                print("Try Again !")
