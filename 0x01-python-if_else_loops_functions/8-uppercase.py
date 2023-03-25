#!/usr/bin/python3

def uppercase(str):
    r = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            r += chr(ord(char) - ord('a') + ord('A'))
        else:
            r += char
    print("{}\n".format(result))
