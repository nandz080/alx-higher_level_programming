#!/usr/bin/python3
"""
method that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    returns  peak in a list of unsorted integers
    """
    for i in range(len(list_of_integers)):
        is_peak = True
        
        if i > 0 and list_of_integers[i] <= list_of_integers[i - 1]:
            is_peak = False
        if i < len(list_of_integers) - 1 and list_of_integers[i] <= list_of_integers[i + 1]:
            is_peak = False
        
        if is_peak:
            return list_of_integers[i]

