"""
Calculate Using String Operation
Create a function that takes two numbers and a mathematical operator and returns the result.

Examples
calculate(4, 9, "+") ➞ 13

calculate(12, 5, "-") ➞ 7

calculate(6, 3, "*") ➞ 18

calculate(25, 5, "//") ➞ 5

calculate(14, 3, "%") ➞ 2

calculate(7, 2, "/") ➞ 3.5
Notes
Numbers can be negative.
The only operations used are those in the examples above.
"""
def calculate(num1, num2, op):
    return eval(str(num1) + op + str(num2))


def calculate(num1, num2, op):
    return eval("{}{}{}".format(num1, op, num2))
