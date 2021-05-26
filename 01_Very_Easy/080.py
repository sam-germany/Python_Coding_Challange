"""
Repeat String
Create a function that takes a string txt and a number n and returns the repeated string n number of times.

If given argument txt is not a string, return Not A String !!

Examples
repeat_string("Mubashir", 2) ➞ "MubashirMubashir"

repeat_string("Matt", 3) ➞ "MattMattMatt"

repeat_string(1990, 7) ➞ "Not A String !!"
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
def repeat_string(txt, n):
    return txt * n if isinstance(txt, str) else 'Not A String !!'


repeat_string = lambda t,n:t*n if type(t) is str else "Not A String !!"
