# Functions go here
def int_check(question):
    """ Checks users enter an integer"""

    error = "Oops - please enter an integer"

    while True:

        try:
            # return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


def not_blank(question):
    """checks that the user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry this cant be blank please try again.\n")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """checks that users enter a full word
    or the n letters of a word from a range of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            #check if the response is the entire word
            if response == item:
                return item

            # check if its the n letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose from {valid_answers}")

# main rourine goes here

# initialise variables / non default options for string vhecker
payment_ans = ('cash', 'credit')

# ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# credit charge suurcharge (currently 5%)
CREDIT_SIRCHARGE = 0.05

# loop for testing purposes
while True:
    print()

    # ask user gor their name (and check its not vlank)
    name = not_blank("Name: ")

    #ask for their age anf check it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age< 12:
        print(f"{name} is too young")

     # child tivket price is 7.50
    elif 12 <= age <16:
        ticket_price = CHILD_PRICE

    elif 16 <= age <65:
        ticket_price = ADULT_PRICE

    elif 65 <= age <121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    #ask user fir payment method ( ash / credit / ca / cr)
    pay_method = string_check("Paymrent method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # if paying by credit calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SIRCHARGE

    # calculate total payable
    total_to_pay = ticket_price + surcharge

    print(f"{name}'s ticket cost is ${ticket_price:.2f}, they  paid by {pay_method}"
          f" so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}\n")