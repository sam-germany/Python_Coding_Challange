"""
Buggy Code
The challenge is to try and fix this buggy code, given the inputs True and False. See the examples below for the expected output.

Examples
has_bugs(True) ➞ "sad days"

has_bugs(False) ➞ "it's a good day"
Notes
Don't overthink this challenge (look at the syntax and correct it).
"""
def has_bugs(buggy_code):
    if buggy_code:
        return 'sad days'
    else:
        return 'it\'s a good day'



def has_bugs(buggy_code):
    if buggy_code:
        return "sad days"
    else:
        return "it's a good day"
