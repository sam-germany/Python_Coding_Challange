"""
Triangle and Parallelogram Area Finder
Write a function that accepts base (decimal), height (decimal) and shape ("triangle", "parallelogram") as input and calculates the area of that shape.

Examples
area_shape(2, 3, "triangle") ➞ 3

area_shape(8, 6, "parallelogram") ➞ 48

area_shape(2.9, 1.3, "parallelogram") ➞ 3.77
Notes
Area of a triangle is 0.5 * b * h
Area of a parallelogram is b * h
Assume triangle and parallelogram are the only inputs for shape.
"""
def area_shape(base, height, shape):
    return base * height / [1, 2][shape == "triangle"]


def area_shape(b,h,f):
    return b*h*0.5 if f=='triangle' else b*h
