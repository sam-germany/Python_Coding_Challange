"""
Convert All List Items to String
Create a function that takes a list of integers and strings. Convert integers to strings and return the new list.

Examples
parse_list([1, 2, "a", "b"]) ➞ ["1", "2", "a", "b"]

parse_list(["abc", 123, "def", 456]) ➞ ["abc", "123", "def", "456"]

parse_list([1, 2, 3, 17, 24, 3, "a", "123b"]) ➞ ["1", "2", "3", "17", "24", "3", "a", "123b"]

parse_list([]) ➞ []
"""
def parse_list(lst):
    return list(map(str, lst))



def parse_list(lst):
    return [str(i) for i in lst]
