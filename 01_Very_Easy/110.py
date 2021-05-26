"""
Cleaning Up Messy Lists
Create a function that takes a list. This list will contain numbers represented as strings.

Your function should split this list into two new lists. The first list should contain only even numbers. The second only odd. Then, wrap these two lists in one main list and return it.

Return an empty list if there are no even numbers, or odd.

Examples
clean_up_list(["8"]) ➞ [[8], []]

clean_up_list(["11"]) ➞ [[], [11]]

clean_up_list(["7", "4", "8"]) ➞ [[4, 8], [7]]

clean_up_list(["9", "4", "5", "8"]) ➞ [[4, 8], [9, 5]]
Notes
All numbers will be positive integers.
"""
def clean_up_list(l):
    e = [int(i) for i in l if not int(i)%2]
    o = [int(i) for i in l if int(i) not in e]
    return [e,o]



def clean_up_list(lst):
    even = [i for i in map(int, lst) if i%2 == 0]
    odd = [i for i in map(int, lst) if i%2 == 1]
    return [even, odd]
