"""
AND, OR and NOT
You will need to write three unfinished logic gates. Continue to write the three logic gates: AND, OR, and NOT.

Examples
AND(1, 1) ➞ 1
AND(0, 0) ➞ 0

OR(1, 0) ➞ 1
OR(1, 1) ➞ 1

NOT(0) ➞ 1
NOT(1) ➞ 0
Notes
Check the Resources tab for some help.
"""
def NOT(num):
    return int(not num)

def AND(num,num2):
    return int(num and num2)

def OR(num,num2):
    return int(num or num2)




def NOT(n):
    return not n
def AND(n1, n2):
    return n1 & n2
def OR(n1, n2):
    return n1 | n2
