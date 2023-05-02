#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle
my = Rectangle(2, 4)
print(my.__dict__)

my.width = 10
my.height = 3
print(my.__dict__)
