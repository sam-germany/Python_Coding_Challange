"""
Return Negative
Create a function that takes a number as an argument and returns negative of that number. Return negative numbers without any change.

Examples
return_negative(4) ➞ -4

return_negative(15) ➞ -15

return_negative(-4) ➞ -4

return_negative(0) ➞ 0
Notes
"""
def return_negative(n):
    return -abs(n)


return_negative = lambda n:-abs(n)
