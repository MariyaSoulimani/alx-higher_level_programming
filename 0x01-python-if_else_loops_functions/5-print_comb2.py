#!/usr/bin/python3
for n in range(0, 100):
    if n < 99:
        print('{}{}'.format(0, n) if n < 10 else '{}'.format(n), end=', ')
    else:
        print(99)
