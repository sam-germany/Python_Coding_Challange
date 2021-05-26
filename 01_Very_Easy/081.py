"""
Check if a List Contains a Given Number
Write a function to check if a list contains a particular number.

Examples
check([1, 2, 3, 4, 5], 3) ➞ True

check([1, 1, 2, 1, 1], 3) ➞ False

check([5, 5, 5, 6], 5) ➞ True

check([], 5) ➞ False
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
def check(lst, el):
    return el in lst

def check(lst, el):
    for i in range(len(lst)):
        if lst[i] == el:
            return True;
    return False;
