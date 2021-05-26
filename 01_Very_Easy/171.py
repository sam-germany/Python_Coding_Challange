"""
Find None in a List
Create a function to find None in a list of numbers. The return value should be the index where None is found. If None is not found in the list, then return -1.

Examples
find_none([1, 2, None]) ➞ 2

find_none([None, 1, 2, 3, 4]) ➞ 0

find_none([0, 1, 2, 3, 4]) ➞ -1
Notes
None will occur in the input list only once.
"""
def find_None(lst):
    return lst.index(None) if None in lst else -1


def find_None(lst):
    try:
        return lst.index(None)
    except ValueError:
        return -1
