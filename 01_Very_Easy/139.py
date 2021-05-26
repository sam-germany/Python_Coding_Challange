"""
Slice of Pie
Create a function that determines whether or not it's possible to split a pie fairly given these three parameters:

Total number of slices.
Number of recipients.
How many slices each person gets.
The function will be in this form:

equal_slices(total slices, no. recipients, slices each)
Examples
equal_slices(11, 5, 2) ➞ True
# 5 people x 2 slices each = 10 slices < 11 slices

equal_slices(11, 5, 3) ➞ False
# 5 people x 3 slices each = 15 slices > 11 slices

equal_slices(8, 3, 2) ➞ True

equal_slices(8, 3, 3) ➞ False

equal_slices(24, 12, 2) ➞ True
Notes
Return (trivially) True if there are zero people.
It's fine not to use the entire pie.
All test parameters are integers.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""
def equal_slices(total, people, each):
    return total >= people * each



def equal_slices(total, people, each):
    return total/each >= people
