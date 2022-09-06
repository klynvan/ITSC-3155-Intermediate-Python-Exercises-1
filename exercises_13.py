def count_letter(usr_string):
    dict = {}
    newstring = usr_string.lower()
    # makes the new string lower case
    for i in newstring:
        keys = dict.keys()
        # retrieve all of the keys from the dictionary
        if i in keys:
            dict[i] += 1
            # counts each time letter repeats
        else:
            dict[i] = 1
    return dict
    # https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php


user_string = str(input('Enter a String: '))
string_dict = count_letter(user_string)
print(string_dict)
