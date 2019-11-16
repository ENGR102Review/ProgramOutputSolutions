# get the highest degree of the polynomial from the user
highest_degree = int(input('Please enter the highest degree in your polynomial (i.e. 3 for a cubic function):'))

# this will hold the user's input for coefficients
# the indexes of each coefficient will match the powers of x that the coefficient is associated with
polynomial_coefficients = []

# start with the highest degree in the polynomial and work down to the constant term
# it is also valid to start at the constant term and go to the highest degree
for i in range(highest_degree, -1, -1):
    user_input = float(input('Enter the polynomial coefficient for the degree %d term:' % i))
    # Since indexes must match powers and the program starts at the highest power, insert new coefficients at the bottom of the list
    polynomial_coefficients.insert(0, user_input)

# the derivative of a constant is 0, so remove it from the list
polynomial_coefficients.pop(0)

# this will hold all terms of the derivative
derivative = []

# start at the highest degree
for i in range(len(polynomial_coefficients) - 1, -1, -1):
    # apply power rule. multiply coefficient by power that was brough down (in this case, i + 1)
    power_rule_coefficient = polynomial_coefficients[i] * (i + 1)
    # skip over terms with a coefficient of 0
    if power_rule_coefficient == 0:
        continue
    # add the term to the list
    derivative.append(str(power_rule_coefficient) + 'x^' + str(i))

# join all terms in the list with a + sign
deriv_string = ' + '.join(derivative)

print('The derivative is', deriv_string)
