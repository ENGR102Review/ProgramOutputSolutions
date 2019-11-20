import matplotlib.pyplot as plt

total_value = 0  # keep a running total of the neighborhood's assessed value
total_price_per_sqft = 0  # keep a running total of price per square foot
houses_after_2000 = 0  # keep a running total of houses built after 2000
most_expensive_value = -9e99  # starter variables for most expensive property
most_expensive_address = ''
total_houses = 0  # keep count of total number of houses so average can be computed later

# use with statement to open file
with open('data.csv') as file:
    file.readline()  # strips off the header (first line)
    for line in file.readlines():  # loop through remaining lines in file
        total_houses += 1  # increment total houses counter
        split_line = line.split(',')  # split the line by a comma character
        # get the values corresponding to each index
        address = split_line[0]
        sqft = float(split_line[1])
        value = float(split_line[2])
        year = int(split_line[3])
        plt.plot(value, sqft, 'b.')  # plots the current point
        # increment houses after 2000 counter if applicable
        if year >= 2000:
            houses_after_2000 += 1
        # update most expensive value and address if applicable
        if value > most_expensive_value:
            most_expensive_value = value
            most_expensive_address = address
        total_price_per_sqft += value / sqft  # add this property's price per sqft to the running total

# calculate average by dividing total price per square foot by the number of houses
average_price_per_sqft = total_price_per_sqft / total_houses

# print descriptive output
print('The average price per square foot is $%.2f' % average_price_per_sqft)
print('%d houses were built after 2000' % houses_after_2000)
print('The address of the most expensive property is %s' % most_expensive_address)

# label title and axes, show plot
plt.xlabel('Property value ($)')
plt.ylabel('Square footage (ft^2)')
plt.title('Square Footage vs. Property Value')
plt.show()
