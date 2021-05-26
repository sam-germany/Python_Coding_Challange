"""
Invert a List
Create a function that takes a list of numbers lst and returns an inverted list.

Examples
invert_list([1, 2, 3, 4, 5]) ➞ [-1, -2, -3, -4, -5]

invert_list([1, -2, 3, -4, 5]) ➞ [-1, 2, -3, 4, -5]

invert_list([]) ➞ []
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
def invert_list(lst):
    return [-i for i in lst]


def invert_list(lst):
    print(lst)
    result = [x * -1 for x in lst]
    return result
