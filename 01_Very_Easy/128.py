"""
Broken Bridge
Create a function which validates whether a bridge is safe to walk on (i.e. has no gaps in it to fall through).

Examples
is_safe_bridge("####") ➞ True

is_safe_bridge("## ####") ➞ False

is_safe_bridge("#") ➞ True
Notes
You can expect the bridge's ends connecting it to its surrounding.
"""
def is_safe_bridge(s):
    return ' ' not in s




def is_safe_bridge(s):
    x = len(s)
    y = s.count("#")
    if x == y:
        return True
    else:
        return False
