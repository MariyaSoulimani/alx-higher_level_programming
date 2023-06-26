#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    while elements < x:
        try:
            print('{}'.format(my_list[elements]), end="")
            elements += 1
        except IndexError:
            break

    print()
    return (elements)
