#!/usr/bin/python3
import sys

args = sys.argv[1:]

add = 0

for arg in args:
    add += int(arg)

print(add)
