"""
Sum of Minimums
Create a function that takes a 2D list lst returns the sum of the minimum value in each row.

Examples
sum_minimums([
  [1, 2, 3, 4, 5],
  [5, 6, 7, 8, 9],
  [20, 21, 34, 56, 100]
] ➞ 26

# minimum value of the first row is 1
# minimum value of the second row is 5
# minimum value of the third row is 20
Notes
N/A
"""
def sum_minimums(lst):
    return sum(min(x) for x in lst)



def sum_minimums(lst):
    return sum(map(min, lst))



def sum_minimums(lst):
    res = 0
    for row in lst:
        res += min(row)
    return res
