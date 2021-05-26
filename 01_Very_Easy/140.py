"""
Does the Dictionary Contain a Given Key?
Write a function that returns True if a dictionary contains the specified key, and False otherwise.

Examples
has_key({ "a": 44, "b": 45, "c": 46 }, "d") ➞ False

has_key({ "craves": True, "midnight": True, "snack": True }, "morning") ➞ False

has_key({ "pot": 1, "tot": 2, "not": 3 }, "not") ➞ True
"""
def has_key(dictionary, key):
    return key in dictionary


def has_key(dictionary, key):
    return key in dictionary.keys()
