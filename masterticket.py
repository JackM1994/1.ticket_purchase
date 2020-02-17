SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

# create the calculate price function. It takes number of tickets and returns
# num_tickets * TICKET_PRICE
def calculate_price(number_of_tickets):
    # create a new const for the 2 dollar service charge
    # Add service charge to our result
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE 


while tickets_remaining >=1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = raw_input("What is your name? ")
    num_tickets = raw_input("How many tickets would you like, {}? ".format(name))
   
    try:
        num_tickets = int(num_tickets)
        # Raise a ValueError if the request is for more tickets than there are
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no ran into an issue. {} . Please try again".format(err))

    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        should_proceed = raw_input("Do you want to proceed? Y/N ")
        if should_proceed.lower() == "y":
            # Todo: gather credit card info and processor
            print("SOLD!")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))
print('Sorry the tickets are all sold out!!!')