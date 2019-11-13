# interpolation between 2D cartesian points
# visualize this example here: https://www.desmos.com/calculator/lkyi2y4kbx

# tuples are a good way to represent point coordinates, since they cannot change
# these are in the format (x, y)
point_A = (20, 16)
point_B = (24, 8)

# now compute the slope of the line connecting the two points
# (y2 - y1) / (x2 - x1)
slope = (point_B[1] - point_A[1]) / (point_B[0] - point_A[0])

# this is an x-value between the x-values of point A and point B
x_value_to_interpolate = 22.5

# this finds the change in x between the interpolation point and the lower x-value of the two original points
change_in_x = x_value_to_interpolate - point_A[0]

# now multiply the change in x by the slope, to find the change in y
delta_y = change_in_x * slope

# add the original y of the first point
y = delta_y + point_A[1]

print('The interpolated value at x = %f is %f' % (x_value_to_interpolate, y))
