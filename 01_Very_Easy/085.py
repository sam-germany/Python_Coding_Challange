"""
On/Off Switches
Create a function that returns how many possible arrangements can come from a certain number of switches (on / off). In other words, for a given number of switches, how many different patterns of on and off can we have?

Examples
pos_com(1) ➞ 2

pos_com(3) ➞ 8

pos_com(10) ➞ 1024
Notes
All numbers will be whole and positive.
"""
def pos_com(num):
    return 2**num


pos_com=lambda n: 2**n
