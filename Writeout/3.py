import math


def f_1(x):
    """
    Represents y = x^2 + 4
    """
    return x ** 2 + 4


def f_2(x):
    """
    Represents y = e^x
    """
    return math.e ** x


x_interval_1 = 3  # size of interval for first function is 5 - 2 = 3
x_interval_2 = 4  # size of interval for second function is 4 - 0 = 4

rectangle_base_1 = x_interval_1 / 60  # the width of each rectangle in first function
rectangle_base_2 = x_interval_2 / 100  # the width of each rectangle in first function

# these will be incremented by the rectangle base each time the program runs
current_x_1 = 2
current_x_2 = 0

# keep a running total of the total area under each curve
total_area_1 = 0
total_area_2 = 0

# compute the area of rectangles in for-loop
for i in range(0, 60):
    # the area of the rectangle is the base multiplied by the function value at the x position
    total_area_1 += rectangle_base_1 * f_1(current_x_1)
    current_x_1 += rectangle_base_1

# compute the area of rectangles in for-loop
for i in range(0, 100):
    # the area of the rectangle is the base multiplied by the function value at the x position
    total_area_2 += rectangle_base_2 * f_2(current_x_2)
    current_x_2 += rectangle_base_2

# print descriptive output
print('The approximate area under x^2 + 4 from 2 to 5 is approximately %.3f' % total_area_1)
print('The approximate area under e^x from 0 to 4 is approximately %.3f' % total_area_2)
