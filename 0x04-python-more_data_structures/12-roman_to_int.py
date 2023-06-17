#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str):
        return (0)
    result = 0
    prev_value = 0
    for i in roman_string:
        if i in roman_dict:
            curr_value = roman_dict[i]
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value
            else:
                result += curr_value
            prev_value = curr_value
        else:
            return (0)
    return (result)
