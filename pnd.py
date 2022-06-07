# Ask user to enter a number called "user_no"
user_no = input('Enter a number: ')

# Validate that user_no is actually a number
try:
    # Runs if the input is valid
    user_no = int(user_no)
    print('You entered a valid input')

# If the number is +ve, print true, else print false
    if user_no >= 0:
        print('True')

    else:
        print('False')
except:
    # Runs if the input is invalid
    print("This is not a number")



