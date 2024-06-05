#Prompt the user.
prompt = f"\nLooking to buy a ticket? Enter your age to get started. "
prompt += f"\nEnter done when finished: "

age = ""
while age != 'done':
    age = input(prompt)
    if age == 'done':  #Stop loop if correct input is entered.
        print("Exit program.")
#Determine the ticket price.
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")

        elif age < 13:
            print("Your ticket is $10.")

        else:
            print("Your ticket is $15.")
