"""
Sum Greater Than Five
Write a function that returns the sum of elements greater than 5, in the given list.

Examples
sum_five([1, 5, 20, 30, 4, 9, 18]) ➞ 77

sum_five([1, 2, 3, 4]) ➞ 0

sum_five([10, 12, 28, 47, 55, 100]) ➞ 252
Notes
Find all the elements greater than 5, not the elements greater than or equal to 5.
"""
def sum_five(l):
    return sum(num for num in l if num > 5)


def sum_five(l):
    return sum(e for e in l if e > 5)
