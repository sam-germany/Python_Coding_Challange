"""
Concatenating Two Integer Lists
Create a function to concatenate two integer lists.

Examples
concat([1, 3, 5], [2, 6, 8]) ➞ [1, 3, 5, 2, 6, 8]

concat([7, 8], [10, 9, 1, 1, 2]) ➞ [7, 8, 10, 9, 1, 1, 2]

concat([4, 5, 1], [3, 3, 3, 3, 3]) ➞ [4, 5, 1, 3, 3, 3, 3, 3]
Notes
Don't forget to return the result.
See Resources tab for more info.
"""
def concat(lst1, lst2):
    return lst1 + lst2


def concat(lst1, lst2):
    lst1.extend(lst2)
    return lst1
