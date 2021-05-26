"""
Fraction Greater Than One
Given a fraction as a string, return whether or not it is greater than 1 when evaluated.

Examples
greater_than_one("1/2") ➞ False

greater_than_one("7/4") ➞ True

greater_than_one("10/10") ➞ False
Notes
Fractions must be strictly greater than 1 (see example #3).
"""
def greaterThanOne(frac):
    return eval(frac) > 1


def greater_than_one(frac):
    frac_lst = frac.split('/')
    return int(frac_lst[0]) > int(frac_lst[-1])
