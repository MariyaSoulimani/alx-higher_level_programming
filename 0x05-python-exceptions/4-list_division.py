#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    i = 0
    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
            div = 0
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
             new_list[i] = div
        i += 1
    return (new_List)
