# FUnctions go here
def string_check(question, valid_ans=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word"""

    while True:


        response = input(question).lower()

        for item in valid_ans:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans}.")

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def instructions():
    make_statement("Instructions",decoration="{}")

    print('''

For each ticket holder enter...
-Their name
-Their age
-The payment method (cash/credit)

The program will record the ticket sale and calculate 
the ticket cost and profit.

Once you have either sold all the  tickets or entered
 the exit code (xxx),the program will display
the ticket sales information and write the data 
to a text file.

It will also choose one lucky ticket holder who wins the draw.
(Their ticket is free)
''')

# Main Routine goes here
make_statement(statement="MMF", decoration="{}")

# Main routine goes here
payment_ans = ('cash', 'credit')

want_instructions = string_check("Do you want to read the instructions")
print(f"You chose {want_instructions}")
if want_instructions == "yes":
    print(f"{instructions()}")

pay_method = string_check("Payment method: ", payment_ans, num_letters=2)
print(f"You chose {pay_method}.")

