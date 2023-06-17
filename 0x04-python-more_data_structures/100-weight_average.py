#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    weight = 0
    average = []
    for tuple in my_list:
        average.append(tuple[1])
        weight += tuple[0] * tuple[1]
    return (weight / sum(average))
