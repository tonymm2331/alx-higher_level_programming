#!/usr/bin/python3

for i in range(ord('a'), ord('z')+1):
    print(chr(i), end="" if chr(i) not in "eq" else "")

