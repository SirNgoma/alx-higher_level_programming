#!/usr/bin/python3
import sys

if __name_ == "__main__":
    args = sys.argv[1:]
    num_of_args = len(args)

    print("{} arguments:".format("" if num_of_args == 1 else "s", num_of_args), end="")
    if num_of_args == 0:
        print(".")
    else:
        print(":")
        for i, arg in enumurate(args):
            print("{}: {}".format(i+1, arg))
