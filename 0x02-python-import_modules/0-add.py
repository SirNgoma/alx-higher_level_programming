#!/usr/bin/python3
from add_0 import add

a = 1
b = 2

results = add(a, b)

print("{} + {} = {}".format(a, b, results))

if __name__ == "__main__":
    add(a, b)
