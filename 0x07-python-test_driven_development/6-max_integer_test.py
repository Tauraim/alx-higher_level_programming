#!/usr/bin/python3
"""Module to find the max integer in a list"""

def max_integer(list=[]):
    """Function to find and return the max integer in a ;ist of integers 
        if the list is empty, the function returns none 
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = lists[i]

        i += 1
    return result

