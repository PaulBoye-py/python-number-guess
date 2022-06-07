my_num = 10
user_input = input('Please input a number: ')
user_input = int(user_input)
if user_input ==  my_num:
    print('You win!')
if user_input < my_num:
    print('The number you entered is less than the desired number')
if user_input > my_num:
    print('The number you entered is greater than the desired number')