import math
import numpy as np


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


# use linspace() function to generate the appropriate x values for the Riemann sum
# function 1 is from x=2 to x=5 with 60 even sub-intervals
x_values_1 = np.linspace(2, 5, 61)
# function 2 is from x=0 to x=4 with 100 even sub-intervals
x_values_2 = np.linspace(0, 4, 101)

# these will keep a running total of the individual rectangle areas
total_area_1 = total_area_2 = 0

# define delta x for both functions. (b-a) / n
delta_x_1 = (5 - 2) / 60
delta_x_2 = (4 - 0) / 100

# go from 0 to the second to last index. Left Riemann sums do not include the rightmost endpoint.
for i in range(len(x_values_1) - 1):
    # add f(xi) * delta x to the total rectangle areas
    total_area_1 += f_1(x_values_1[i]) * delta_x_1

for i in range(len(x_values_2) - 1):
    # add f(xi) * delta x to the total rectangle areas
    total_area_2 += f_2(x_values_2[i]) * delta_x_2

# print descriptive output
print('The approximate area under x^2 + 4 from 2 to 5 is approximately %.3f' % total_area_1)
print('The approximate area under e^x from 0 to 4 is approximately %.3f' % total_area_2)
