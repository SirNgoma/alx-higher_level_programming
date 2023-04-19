#!/usr/bin/python3
import sys

if __name_ == "__main__":
    num_of_args = len(sys.argv) - 1

    print(f"{} arguments{'s' if num_of_args != 1 else ''}: {num_of_args}", end="")
    if num_of_args == 0:
        print("0 arguments")
    elif num_of_args == 1:
        print("1 argument")
    else:
        print(":")
        for i, in range(1, num_of_args + 1):
            print(f"{i}: {sys.argv[i]}")
