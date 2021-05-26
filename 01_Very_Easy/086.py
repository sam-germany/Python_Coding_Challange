"""
Is the Last Character an "N"?
Create a function that takes a string (a random name). If the last character of the name is an "n", return True, otherwise return False.

Examples
is_last_character_n("Aiden") ➞ True

is_last_character_n("Piet") ➞ False

is_last_character_n("Bert") ➞ False

is_last_character_n("Dean") ➞ True
Notes
The function must return a boolean value ( i.e. True or False).
"""
def is_last_character_n(word):
    return word.endswith('n')

def is_last_character_n(word):
    return word[-1] == 'n'
