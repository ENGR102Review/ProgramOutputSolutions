# example data for the first 10 elements on the periodic table
names = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
weights = [1.008, 4.002, 6.94, 9.012, 10.81, 12.011, 14.007, 15.999, 18.998, 20.18]
symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']

# use a with statement and be sure to specify write mode with the 'w' parameter in the open() function
# the file object will be called data_file
with open('periodic_data.csv', 'w') as data_file:
    # this is the header, goes on first line of file
    data_file.write('Atomic Number,Name,Symbol,Weight (amu)\n')  ## do not forget the \n at the end!
    for i in range(0, 10):
        # you must cast all non-string types to strings.
        # e.g. data_file.write(i + 1) would produce an error, since i is an int, not a string.
        # separate each component of the line by commas.
        # place a newline character at the very end of the line.
        data_file.write(str(i + 1) + ',' + names[i] + ',' + symbols[i] + ',' + str(weights[i]) + '\n')
