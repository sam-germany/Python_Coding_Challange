"""
Even or Odd?
Given a list of integers, determine whether the sum of its elements is even or odd.

The return value should be a string ("odd" or "even").

If the input list is empty, consider it as a list with a zero ([0]).

Examples
even_or_odd([0]) ➞ "even"

even_or_odd([1]) ➞ "odd"

even_or_odd([]) ➞ "even"

even_or_odd([0, 1, 5]) ➞ "even
"""
def even_or_odd(lst):
    return 'odd' if sum(lst) % 2 else 'even'


def even_or_odd(lst):

    Total = 0

    for x in lst:
        Total += x

    if (Total % 2 == 0):
        return "even"
    else:
        return "odd"
