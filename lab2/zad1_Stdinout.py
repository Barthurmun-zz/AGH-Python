#!/usr/bin/python3

import sys

arg = sys.stdin.readline()

print(arg)

file = open("NewFile.txt","w")
file.write(arg)
file.close()