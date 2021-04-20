##This code validates if the user's input is a number, it's type or it's a string
##So far no library's needed

##Method that performs the validation
def ValidateInput(user_input):
    try:
        # Verify input is an integer by direct casting
        is_int = int(user_input)
        print("Input is an integer: ", is_int)
    except ValueError:
        try:
            # Verify input is a float by direct casting
            if_float = float(user_input)
            print("Input is a float: ", if_float)
        except ValueError:
            print("It's a string or NaN (Not a Number)") 

user_input = 'i' ##Initilize
##User input will be solicited and validated until user types an enter
while( user_input.strip() != '' ):
    user_input = raw_input("Please type a number. Enter to exit: ")
    ValidateInput(user_input)   