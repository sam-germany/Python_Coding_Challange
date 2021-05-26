"""
Sum of Cubes
Create a function that takes a positive integer n, and returns the sum of all the cubed values from 1 to n.

For example, if n is 3:

sum_cubes(3) ➞ 36
1 ** 3 + 2 ** 3 + 3 ** 3 = 36
Examples
sum_cubes(7) ➞ 784

sum_cubes(8) ➞ 1296

sum_cubes(9) ➞ 2025
Notes
Input n will be a positive integer.
"""
def sum_cubes(n):
    return sum(i ** 3 for i in range(1, n + 1))



def sum_cubes(n):
    return ((n*(n+1))//2)**2
