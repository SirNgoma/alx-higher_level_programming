#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1

    a = 10
    b = 5

    adds = calculator_1.add(a, b)
    substract = calculator_1.sub(a, b)
    multi = calculator_1.mul(a, b)
    divide = calculator_1.div(a, b)

    print("{} + {} = {}".format(a, b, adds))
    print("{} - {} = {}".format(a, b, substract))
    print("{} * {} = {}".format(a, b, multi))
    print("{} / {} = {}".format(a, b, divide))
