# here is a list of numbers
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]

# if you wanted to go through the list backwards:

# you could use the downward counting loop approach
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i])

# or you could use the negative indexes approach
for i in range(1, len(my_list) + 1):
    print(my_list[-i])

# or you could use python's built in reversed() function
# note that this goes through elements, not indexes!
for element in reversed(my_list):
    print(element)
