
# Initialise Ticket Numbers
MAX_TICKETS = 5
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You  have sold max tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} /{MAX_TICKETS} tickets")