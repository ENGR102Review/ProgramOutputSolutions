# two parallel lists that contain name and age data
names_list = ['Dave', 'John', 'Bob', 'Sylvester']
age_list = [24, 52, 39, 67]

# print a header
print('Name'.ljust(15) + 'Age')

# iterate through the lists
for i in range(len(names_list)):
    # get the name, left justify it by 15 spaces
    # get the corresponding age, print it after the justified name
    print(str(names_list[i]).ljust(15) + str(age_list[i]))


print()

# alternatively, if you wanted to right-justify:
print('Name'.rjust(15) + 'Age'.rjust(15))
# iterate through the lists
for i in range(len(names_list)):
    # get the name, right justify it by 15 spaces
    # get the corresponding age, right justify by 15 spaces
    print(str(names_list[i]).rjust(15) + str(age_list[i]).rjust(15))
