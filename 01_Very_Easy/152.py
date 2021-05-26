"""
Random Integer Generator
The challange is simple. Return a random integer N such that a <= N <= b.

Examples
random_int(5, 9) ➞ 7

random_int(5, 9) ➞ 9

random_int(5, 9) ➞ 5
Notes
Don't forget to return the result.
Return value must be an integer.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
from random import randint as random_int


from random import randint
def random_int(a, b):
    return randint(a,b)



import random
def random_int(a, b):
    return random.randint(a, b)
