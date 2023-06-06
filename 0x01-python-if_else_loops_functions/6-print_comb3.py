#!/usr/bin/python3
print(', '.join('{}{}'.format(a, b) for a in range(9) for b in range(a+1, 10)))
