i = 0
sum = 0
while i < 5:
    usr_in = input(f'Enter int #{i+1}: ')
    try:
        usr_int = int(usr_in)
        is_int = True
    except ValueError:
        # excepts blocks prints msg and re runs
        #https://bobbyhadz.com/blog/python-only-allow-integer-user-input#:~:text=To%20only%20allow%20integer%20user,user%20entered%20to%20an%20integer.
        print('Invalid input. Please enter a int.')
        is_int = False
    if is_int == True:
        sum += usr_int
        i += 1

print(sum)
