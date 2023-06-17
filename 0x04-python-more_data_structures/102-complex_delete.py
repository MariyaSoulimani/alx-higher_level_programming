#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = [key for key, dic_val in a_dictionary.items() if dic_val == value]
    for key in keys:
        del a_dictionary[key]
    return (a_dictionary)
