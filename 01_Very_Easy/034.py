"""
Buggy Code (Part 3)
Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.

Examples
sum_lst([1, 2, 3, 4, 5]) ➞ 15

sum_lst([-1, 0, 1]) ➞ 0

sum_lst([0, 4, 8, 12]) ➞ 24
Notes
READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
Don't overthink this challenge; it's not supposed to be hard.
"""
sum_lst = sum


def sum_lst(lst):
    total = 0
    for i in range(0,len(lst)):
        total += lst[i]
    return total
