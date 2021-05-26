"""
Find the Smallest Number in a List
Create a function that takes a list of numbers and returns the smallest number in the list.

Examples
find_smallest_num([34, 15, 88, 2]) ➞ 2

find_smallest_num([34, -345, -1, 100]) ➞ -345

find_smallest_num([-76, 1.345, 1, 0]) ➞ -76

find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) ➞ -0.9999

find_smallest_num([7, 7, 7]) ➞ 7
Notes
Test cases contain decimals.
If you get stuck on a challenge, find help in the Resources ta
"""
def find_smallest_num(lst):
    return min(lst)

def find_smallest_num(lst):
    lst.sort()
    return lst[0]
