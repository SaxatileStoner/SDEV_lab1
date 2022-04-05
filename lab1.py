'''
* SDEV 300 Building Secure Python Apps
* Lab 1 Assignment
* @author Christopher Stoner

* Python application that supports voter registration
* REQUIREMENTS:
    * PROMT:
        * first name,
        * last name,
        * age,
        * country of citizenship,
        * state of reisdence,
        * ZIP code
    * ERROR CHECKING:
        * ALL fields MUST be entered
        * If they are >= 18 in age, let them continue, if not, do NOT let the user continue
        * Users are probably not > 120 in age
        * states should be 2 letters representing only valid US states
        * Should repromt for data if data is incorrect
'''

import string


def check_yes_no(user_ans: str):
    """checks string if a user inputed yes or no

    Args:
        user_ans (str): contains user string

    Returns:
        is_accepted (bool): determines if the user has input yes or no
    """
    acceptable_ans = ["y", "n", "yes", "no"]
    is_accepted = False
    for answer in acceptable_ans:
        if user_ans.lower() == answer:
            is_accepted = True
            break
    return is_accepted


def check_special_chars(str_input: str):
    """Checks each character in a string against
    punctuation/special characters. If punctuation/special
    character is found, will return true
    Args:
        str_input (str): String to be checked
    Returns:
        has_special_chars (bool): determines if the string contains punctuation/special chars
    """
    has_special_chars = False
    special_list = list(r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~)")
    input_char_list = list(str_input)

    for special_char in special_list:
        for input_char in input_char_list:
            if input_char == special_char:
                has_special_chars = True
                break
        if has_special_chars:
            break
    return has_special_chars


def cannot_contain_s_chars(promt: str):
    """Prints that the string previously inputted
    cannot have special characters. Repromts and
    asks for input based on the promt arg.
    Args:
        promt (str): promt to be reprinted
    Returns:
        input(promt): prints promt arg and take in input
    """
    print("This CANNOT contain special characters!")
    return input(promt)


def check_num_chars(str_input: str):
    """Checks each character in a string against digits (0-9)
    If an digit is found, will return true
    Args:
        str_input (str): String to be checked
    Returns:
        has_num_chars (bool): determines if the string contains digits (0-9)
    """
    has_num_chars = False
    num_list = list(string.digits)
    input_char_list = list(str_input)

    for num_char in num_list:
        for input_char in input_char_list:
            if input_char == num_char:
                has_num_chars = True
                break
        if has_num_chars:
            break
    return has_num_chars


def cannot_contain_num_chars(promt: str):
    """Prints that the string previously inputted
    cannot have num characters. Repromts and
    asks for input based on the promt arg.
    Args:
        promt (str): promt to be reprinted
    Returns:
        input(promt): prints promt arg and take in input
    """
    print("This CANNOT contain digit characters!")
    return input(promt)


def check_letter_chars(str_input: str):
    """Checks each character in a string against ascii letters
    If an ascii letter is found, will return true
    Args:
        str_input (str): String to be checked
    Returns:
        has_letter_chars (bool): determines if the string contains ascii letters
    """
    has_letter_chars = False
    letter_list = list(string.ascii_letters)
    input_char_list = list(str_input)

    for letter_char in letter_list:
        for input_char in input_char_list:
            if input_char == letter_char:
                has_letter_chars = True
                break
        if has_letter_chars:
            break
    return has_letter_chars


def cannot_contain_letter_chars(promt: str):
    """Prints that the string previously inputted
    cannot have letter characters. Repromts and
    asks for input based on the promt arg.
    Args:
        promt (str): promt to be reprinted
    Returns:
        input(promt): prints promt arg and take in input
    """
    print("This CANNOT contain letter characters!")
    return input(promt)


def check_two_letters_only(str_input: str):
    """Checks if the inputted string has ONLY two ASCII letters
    Args:
        str_input (str): String to check for ONLY two ASCII type letters
    Returns:
        bool: True: has ONLY two ASCII type letters,
              False: contains more than two length OR contains nums or special chars
    """
    has_two_letters_only = False
    if str_input.__len__() == 2:
        if not check_num_chars(str_input):
            if not check_special_chars(str_input):
                has_two_letters_only = True

    return has_two_letters_only


def check_five_digits_only(str_input: str):
    """Checks if the inputted string has ONLY 5 total digits (0-9)
    Args:
        str_input (str): String to be checked for ONLY 5 total digits
    Returns:
        bool: True: inputted string has ONLY 5 total digits
              False: inputted string DOES NOT have 5 total digits
    """
    has_five_digits_only = False
    if str_input.__len__() == 5:
        if not check_special_chars(str_input):
            if not check_letter_chars(str_input):
                has_five_digits_only = True
    return has_five_digits_only


def check_valid_state(state_str: str):
    """Checks against the two character string
    against an array of us state abbreviations
    Args:
        state_str (str): String to be checked
    Returns:
        bool: True: The string inputted is a US state
              False: The string inputted is NOT a US state
    """
    flag = False
    us_state_array = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE',
                      'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL', 'IN', 'IA',
                      'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS',
                      'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
                      'ND', 'MP', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC',
                      'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'VI', 'WA', 'WV',
                      'WI', 'WY']
    for state in us_state_array:
        if state_str == state:
            flag = True
    return flag


def ask_user_continuation():
    """Checks if a user wishes to continue the program.
    Returns:
        bool : True: Wishes to continue the program, False: Wishes to stop the program
    """
    flag = False
    user_continue = input(
        "Do you want to continue with Voter Registration? Y/N\n")
    while not check_yes_no(user_continue):
        user_continue = input(
            "Do you want to continue with Voter Registration? Y/N\n")
    if user_continue.lower() == "yes" or user_continue.lower() == "y":
        flag = True
    return flag


def print_voter_info(first_name: str, last_name: str, age: int, voter_state: str, zip_code: int):
    """prints the final output from all the inputted information from the user
    Args:
        first_name (str): _description_
        last_name (str): _description_
        age (int): _description_
        voter_state (str): _description_
        zip_code (int): _description_
    """
    print(f"Thanks for registering to vote! Here is the information we received:\n\
            Name (first last): {first_name} {last_name}\n\
            Age: {age}\n\
            U.S. Citzen: Yes\n\
            State: {voter_state}\n\
            Zipcode: {zip_code}\n\
            Thanks for trying the Voter Registration Application!\n\
            Your voter registration card should be shipped within 3 weeks.")


def __main__():
    """Main function containing logical flow of the program
    """
    print("Welcome to the Python Voter Registration Application!")
    # This statement (and others below) checks if the user would
    # like to continue with the register process.
    if ask_user_continuation():

        # FIRST NAME PROMT
        first_name = input("What is your first name?")
        # Checks if first_name contains special character
        while check_special_chars(first_name):
            first_name = cannot_contain_s_chars("What is your first name?")
        # Checks if first_name contains digits
        while check_num_chars(first_name):
            first_name = cannot_contain_num_chars("What is your first name?")

        if ask_user_continuation():

            # LAST NAME PROMT
            last_name = input("What is your last name? ")
            # Checks if last_name contains special characters
            while check_special_chars(last_name):
                last_name = cannot_contain_s_chars("What is your last name?")
            # Checks if last_name contains digits
            while check_num_chars(last_name):
                last_name = cannot_contain_num_chars("What is your last name?")

            if ask_user_continuation():

                # AGE PROMT
                age = input("What is your age? ")
                # Checks if age contains letters
                while check_letter_chars(age):
                    age = cannot_contain_letter_chars("What is your age? ")
                # Checks if age contains special chars
                while check_special_chars(age):
                    age = cannot_contain_s_chars("What is your age? ")

                while int(age) > 120:
                    # No way someone is >120???
                    print(f"Um, no way you're {age}...")
                    age = input("What is your age? ")
                    # Checks if age contains letters
                    while check_letter_chars(age):
                        age = cannot_contain_letter_chars("What is your age? ")
                    # Checks if age contains special chars
                    while check_special_chars(age):
                        age = cannot_contain_s_chars("What is your age? ")

                # Primary Continuation if age is >= 18
                if int(age) >= 18:

                    if ask_user_continuation():

                        # US CITIZEN PROMT
                        is_us_citizen = input("Are you a US citzen? ")
                        # Checks if the user has input yes or no
                        while not check_yes_no(is_us_citizen):
                            is_us_citizen = input("Are you a US citzen? Y/N\n")
                        if is_us_citizen.lower() == 'yes' or is_us_citizen.lower() == 'y':
                            # User MUST be a US citzen to continue

                            if ask_user_continuation():

                                # VOTER STATE PROMT
                                voter_state = input(
                                    "What state do you live in? ")
                                # Check for two letters in the string only
                                while not check_two_letters_only(voter_state):
                                    voter_state = input(
                                        "What state do you live in? ")
                                # Check if those accepted two letters are a valid state
                                # NOTE Possible bug with being able to submit a non valid
                                # state, then not be able to check if the
                                # string is two letters again. It'll detect the string
                                # as a not valid state despite this, so,
                                # functionally not broken, but not design intended.
                                # POSSIBLE FIX: check for two letters only in the check_valid_state
                                # function rather than in  __init__
                                while not check_valid_state(voter_state):
                                    print("That is not a valid state!")
                                    voter_state = input(
                                        "What state do you live in? ")

                                if ask_user_continuation():
                                    # ZIP CODE PROMT
                                    zip_code = input(
                                        "What is your 5 digit zipcode? ")
                                    # Check if zip_code is a five digit number
                                    while not check_five_digits_only(zip_code):
                                        print(
                                            "Your area code MUST be FIVE DIGITS only")
                                        zip_code = input(
                                            "What is your 5 digit zipcode? ")

                                    # FINISHED REGISTER, OUTPUT RESULT TO CLI
                                    print_voter_info(first_name, last_name, int(
                                        age), voter_state, zip_code)
                        # This user is NOT a US citzen!
                        else:
                            print(
                                "Sorry, but only U.S. citzens can apply for voter registration.")
                else:
                    # This user is too young to vote!
                    print(
                        "I am sorry, but you are too young to register.\
                        Come back when you're 18 or older!")
            # END
    print("\nThank you for using the Python Voter Registration Application. Goodbye!")


__main__()
