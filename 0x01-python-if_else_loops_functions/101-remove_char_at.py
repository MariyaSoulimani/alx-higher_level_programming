#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    r = str[0:n]
    r += str[n+1:]
    return r
