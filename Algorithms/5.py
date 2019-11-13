my_grades = [56, 71, 74, 75, 61, 55, 53, 90, 96, 88, 59, 64, 67, 62, 77, 70, 89, 60, 57, 87]

# these are starter variables.
# notice they are outside of the for-loop

# before you even start going through the list, you haven't summed anything, so the sum is 0
sum_of_items = 0
# for now, assume that the first element is the smallest (this can change later)
minimum = my_grades[0]

# for now, assume that the first element is the largest (this can change later)
maximum = my_grades[0]

# loop through all grades in the list
for grade in my_grades:
    # add the current grade to the running total
    sum_of_items += grade
    # check if the current grade is less than the current minimum
    if grade < minimum:
        # if so, set the minimum equal to the current grade
        minimum = grade
    # check if the current grade is greater than the current maximum
    if grade > maximum:
        # if so, set the maximum equal to the current grade
        maximum = grade

# divide the sum by the length of the list to calculate the average
average = sum_of_items / len(my_grades)

# print descriptive output
print('The lowest grade is', minimum)
print('The highest grade is', maximum)
print('The average grade is', average)
