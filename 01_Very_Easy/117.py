"""
Back to Home?
Mubashir has started his journey from home. Given a string of directions (N=North, W=West, S=South, E=East), he will walk for one minute in each direction. Determine whether a set of directions will lead him back to the starting position or not.

Examples
back_to_home("EEWE") ➞ False

back_to_home("NENESSWW") ➞ True

back_to_home("NEESSW") ➞ False
Notes
N/A
"""
def back_to_home(d):
    return d.count('N') == d.count('S') and d.count('E') == d.count('W')


def back_to_home(d):
    return d.count('N') == d.count('S') and d.count('E') == d.count('W')
