def get_combined_dict(dict1, dict2):
    new_dict = {}
    value = 0
    for i in dict1:
        for j in dict2:
            if i == j:
                value = dict1[i] + dict2[j]
                # adds the value from both dictionary
                new_dict.update({i: value})
                # updates the dictionary with the elements from another dictionary object
                # https://www.geeksforgeeks.org/python-dictionary-update-method/
    return new_dict


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
