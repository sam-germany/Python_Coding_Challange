"""
Leap Year Function ⌚
Write a function that returns True if a year is a leap, otherwise return False.

A year is a "leap year" if it lasts 366 days, instead of 365 in a typical year. That extra day is added to the end of the shortest month, creating February 29.

A leap year occurs every four years, and will take place if the year is a multiple of four. The exception to this is a year at the beginning of a century (for example, 1900 or 2000), where the year must be divisible by 400 to be a leap year.

Look at the examples, and if you need help, look at the resources panel.

Examples
leap_year(1990) ➞ False

leap_year(1924) ➞ True

leap_year(2021) ➞ False
Notes
Do not overthink this challenge.
You can solve the problem with a few lines of code.
"""
from calendar import isleap as leapYear


def leapYear(year):
    return year%400==0 or year%100!=0 and year%4==0
