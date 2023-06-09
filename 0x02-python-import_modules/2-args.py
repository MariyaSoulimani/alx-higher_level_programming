#!/usr/bin/python3

if __name__ == "__main__":

import sys

args = sys.argv[1:]
n_args = len(args)

if n_args == 0:
    print("0 arguments.")
elif n_args == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(n_args))

for i in range(n_args):
    print("{}: {}".format(i + 1, args[i]))
