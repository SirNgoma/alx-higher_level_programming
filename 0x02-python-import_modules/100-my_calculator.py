#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        res = add(a, b)
    elif operator == '-':
        res = sub(a, b)
    elif operator == '*':
        res = mul(a, b)
    elif operator == '/':
        res = div(a, b)
    else:
        print("Unknown operator. Available operators; +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, res))
