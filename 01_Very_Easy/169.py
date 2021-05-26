"""
Find the Total Number of Digits the Given Number Has
Create a function that takes a number as an argument and returns the amount of digits it has.

Examples
find_digit_amount(123) ➞ 3

find_digit_amount(56) ➞ 2

find_digit_amount(7154) ➞ 4

find_digit_amount(61217311514) ➞ 11

find_digit_amount(0) ➞ 1
Notes
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
def find_digit_amount(num):
    return (len(str(abs(num))))


def find_digit_amount(num):
    return len(str(num))
