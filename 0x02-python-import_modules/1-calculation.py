#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5

adds = add(a, b)
substract = sub(a, b)
multi = mul(a, b) 
divide = div(a, b)

print("{} + {} = {}".format(a, b, adds))
print("{} - {} = {}".format(a, b, substract))
print("{} * {} = {}".format(a, b, multi))
print("{} / {} = {}".format(a, b, divide))
