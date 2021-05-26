"""
Is the String Odd or Even?
Given a string, return True if its length is even or False if the length is odd.

Examples
odd_or_even("apples") ➞ True
# The word "apples" has 6 characters.
# 6 is an even number, so the program outputs True.

odd_or_even("pears") ➞ False
# "pears" has 5 letters, and 5 is odd.
# Therefore the program outputs False.

odd_or_even("cherry") ➞ True
Notes
N/A
"""
def odd_or_even(str):
    return not len(str) % 2


def odd_or_even(word):
    return len(word) % 2 == 0
