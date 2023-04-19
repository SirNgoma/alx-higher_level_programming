#!/usr/bin/python3
import sys

if __name_ == "__main__":
    args = sys.argv[1:]
    num_of_args = len(args)

    print("{} arguments:".format("" if num_of_args == 1 else "s", num_of_args), end="")
    if num_of_args == 0:
        print("0 arguments")
    elif num_of_args == 1:
        print("1 argument")
    else:
        print(":")
        for i, arg in enumurate(args):
            print("{}: {}".format(i+1, arg))
