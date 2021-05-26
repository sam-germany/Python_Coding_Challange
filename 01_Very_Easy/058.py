"""
Two Makes Ten
Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10.

Examples
makes10(9, 10) ➞ True

makes10(9, 9) ➞ False

makes10(1, 9) ➞ True
Notes
Don't forget to return the result.
"""
def makes10(a, b):
    return 10 in [a, b, a+b]


def makes10(a, b):
    return 10 in (a,b,a+b)
