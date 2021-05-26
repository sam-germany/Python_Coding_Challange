"""
Return the First and Last Elements in a List
Create a function that takes a list of values and returns the first and last values in a new list.

Examples
first_last([5, 10, 15, 20, 25]) ➞ [5, 25]

first_last(["edabit", 13, None, False, True]) ➞ ["edabit", True]

first_last([None, 4, "6", "hello", None]) ➞ [None, None]
Notes
Test input will always contain a minimum of two elements within the list.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
def first_last(lst):
    return [lst[0], lst[-1]]


def first_last(lst):
    del lst[1:-1]
    return lst
