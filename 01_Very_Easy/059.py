"""
Is the String Empty?
Create a function that returns True if a string is empty and False otherwise.

Examples
is_empty("") ➞ True

is_empty(" ") ➞ False

is_empty("a") ➞ False
Notes
A string containing only whitespaces " " does not count as empty.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
def is_empty(s):
    return not s


def is_empty(s):
    return s == ''
