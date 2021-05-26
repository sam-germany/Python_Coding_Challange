"""
Minimal VII: Lambda Functions
Check the principles of minimalist code in the intro to the first challenge.

In the Code tab you will find a code that is missing a single character in order to pass the tests. However, your goal is to submit a function as minimalist as possible. Use the tips in the tips section below.

Write five adder functions:

add_2(x) should return 2 + x.
add_3(x) should return 3 + x.
add_5(x) should return 5 + x.
add_7(x) should return 7 + x.
add_11(x) should return 11 + x.
Tips
Functions that consists only of a return, can be written as oneliner with a lambda function.

For example, the code:

def are_same(a, b):
    return a == b
Can be simplified to:

are_same = lambda a, b: a == b
Bonus
lambda a, b: a == b is technically an anonymous function. However, it can be assigned to the identifier are_same and it can then be called using are_same().

Notes
This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your suggestions in the Comments.
Readability is indeed a subjective concept. Let's discuss it! Feel free to leave your opinion in the Comments.
You can find all the exercises in this series over here.
"""
for n in range(12):exec("add_%s=lambda x:x+%s"%(n,n))



adder = lambda x: lambda y: x+y
add_2 = adder(2)
add_3 = adder(3)
add_5 = adder(5)
add_7 = adder(7)
add_11 = adder(11)
