#!/usr/bin/python3
for num in range(99):
    if num < 99:
        print("{}{}".format(0, num) if num < 10 else '{}'.format(num), end=', ')
    else:
        print(99)
