# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer"

    while True:

        try:
            # Return response if it's an integer
            response = int (input(question))

            return response

        except ValueError:
            print(error)

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry this cant bbe blank. Please try again.\n")

def string_check(question, valid_answers=('yes', 'no'),
                num_letters=1):
    """Checks that users enter a full word
    or the 'n' letters of a word from a range of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the n letters
            elif response ==item[:num_letters]:
                return  item

        print(f"Please choose an option from {valid_answers}")

# main routine goes here

# Initialise variables / non default  options for string checker
payment_ans = ('cash', 'credit')

#loop for testing purposes
while True:
    print()

    # ask user for their name
    name = not_blank("Name:") # replace with call to not blank function

    # ask user for their name  and age and check if its between 12 and 120
    age = int_check("Age: ")

    # output error message /success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    pay_method = string_check("payment method: ", payment_ans, 2)
    print(f"{name} has bought a ticket ({pay_method})")