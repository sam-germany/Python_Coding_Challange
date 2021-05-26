"""
Mumbling Challenge
Create a function that takes a string s and modifies the given string as per the below examples:

Examples
mumbling("MubAshIr") ➞ "M-Uu-Bbb-Aaaa-Sssss-Hhhhhh-Iiiiiii-Rrrrrrrr"

mumbling("maTT") ➞ "M-Aa-Ttt-Tttt"

mumbling("EdaBit") ➞ "E-Dd-Aaa-Bbbb-Iiiii-Tttttt"
Notes
N/A
"""
def mumbling(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


def mumbling(s):
    res = "";
    for i in range(len(s)):
        res += s[i].upper() + s[i].lower() * i + "-"
    return res[:-1]



def mumbling(s):
    return '-'.join(((i + 1) * j).title() for i, j in enumerate(s))
