"""
Divides Evenly
Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.

Examples
divides_evenly(98, 7) ➞ True
# 98/7 = 14

divides_evenly(85, 4) ➞ False
# 85/4 = 21.25
Notes
a will always be greater than or equal to b.
"""
def divides_evenly(a, b):
    return a % b == 0

def divides_evenly(a, b):
    if (a %  b == 0):
        return True
    else:
        return False
