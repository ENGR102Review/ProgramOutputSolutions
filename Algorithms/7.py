# this is calculating the following sigma expression:
# https://us-static.z-dn.net/files/dbb/a31b73f5f35f6b532e67d375f037795e.png


total_sum = 0

# start at n = 2, but notice that 92 is the upper bound, not 91
# this is because you stop iterating at 91, inclusive
for n in range(2, 92):
    # now use n in the expression following the sigma symbol and add it to the total
    total_sum += (3 * n + 8)
