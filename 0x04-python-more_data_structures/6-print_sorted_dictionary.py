#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    sorted_dict = dict(sorted(a_dictionary.items()))
    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))
