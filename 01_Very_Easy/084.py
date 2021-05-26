"""
Check if All Values Are True
Create a function that returns True if all parameters are truthy, and False otherwise.

Examples
all_truthy(True, True, True) ➞ True

all_truthy(True, False, True) ➞ False

all_truthy(5, 4, 3, 2, 1, 0) ➞ False
Notes
Truthy values include non-empty sequences, numbers (except 0 in every numeric type), and basically every value that is not falsy.
You can check if an item is truthy by using an if statement on that item.
You will always be supplied with at least one parameter.
"""
def all_truthy(*args):
    return all(args)


def all_truthy(*args):
    my_list = []
    for i in args:
        if i:
            my_list.append(True)
        else:
            my_list.append(False)
    if False in my_list:
        return False
    else:
        return True
