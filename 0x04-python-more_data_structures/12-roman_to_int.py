#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for c in roman_string:
        if c in dic:
            curr_value = dic[c]
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value
            else:
                result += curr_value
            prev_value = curr_value
        else:
            return 0
    return result
