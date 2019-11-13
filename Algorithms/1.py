# a list to hold user input
name_list = []

# give your user clear instructions on how to use this program
print('Enter as many names as you want. Type \'stop\' when you are done entering names.')

# take an initial input from the user
current_input = input('Please enter your name:')

# loop until the user's input contains the word stop
while 'stop' not in current_input:
    # append the current user's input to the list
    name_list.append(current_input)
    # be sure to update your input for the next iteration of the loop!
    current_input = input('Please enter your name:')
