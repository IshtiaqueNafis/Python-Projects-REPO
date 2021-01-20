TICKET_PRICE = 10  # this is the constanct price

tickets_remaining = 100  # ticket remaning

print(f"there are currently {tickets_remaining}")

# gather the username and assgin to a new variable.


# calulate price
while tickets_remaining:

    user_name = input("what is your name? ")
    print(user_name)

    # pomot the userby name and how many tickets would they like
    tickets_quantity = input('how many tickets would you like?')
    amount = int(tickets_quantity) * TICKET_PRICE

    print(f"ticket price is {amount}")

    # promot user if they want to proceed
    user_input = input("do you want to proceed?")
    if user_input.lower() == 'y':
        print("SOLD")
        tickets_remaining -= int(tickets_quantity);
    else:
        print(f"thank you anyways {user_name}")

    if tickets_remaining == 0:
        print("soryy we have no tickets left")
    else:
        print(f"we still have {tickets_remaining}")
# if they want to proceed
# print(sold)
