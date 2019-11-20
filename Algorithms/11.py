# a list to sort
my_list = [56, 71, 74, 75, 61, 55, 53, 90, 96, 88, 59, 64, 67, 62, 77, 70, 89, 60, 57, 87]

print('Original list:')
print(my_list)

# this list will eventually hold all of the numbers in order.
# it contains one very large number as a "starter" for this algorithm
my_list_sorted = [9e99]


### fake bubble sort algorithm ###
# loop until there are no more elements in the list
while len(my_list) > 0:
    # pop the last element off the list to be sorted
    current_element = my_list.pop()
    # loop through all existing indexes in the sorted list
    for index in range(len(my_list_sorted)):
        # if you find that the number in the sorted list is greater than the current number
        if my_list_sorted[index] > current_element:
            # "push" it forward in the list by inserting the current element behind it
            my_list_sorted.insert(index, current_element)
            # you don't want this to run more than once, so break out of this loop
            break

# the 9e99 will have "bubbled" to the top of the sorted list, but obviously you don't want it.
my_list_sorted.pop()

print('Sorted list:')
print(my_list_sorted)
