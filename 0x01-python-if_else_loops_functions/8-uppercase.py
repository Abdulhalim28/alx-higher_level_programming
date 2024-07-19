#!/usr/bin/python3
def uppercase(str):
for c in str:
 if ord('a') <= ord(c) <= ord('z'):
 print("%c" % (ord(c) - 32), end='')
 else:
     print("%c" % ord(c), end='')
 print()

