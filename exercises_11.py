def get_unique_list(usr_list):
    uni_quelist = []
    for i in usr_list:
        if i not in uni_quelist:
            # checks to see if it not already in x
            uni_quelist.append(i)
            # adds value to new list
    return uni_quelist
# https://www.w3resource.com/python-exercises/python-functions-exercise-8.php


my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unisue_list(my_list)
# print(my_list)
print(unique_list)
