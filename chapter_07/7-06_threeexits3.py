#In this exercise you must exit the loop using a break using existing exercises.

#Prompt the user.
prompt = f"\nLooking to buy a ticket? Enter your age to get started. "
prompt += f"\nEnter done when finished: "

active = True

while active:
    age = input(prompt)
    if age == 'done':  #Stop loop if correct input is entered.
        break

    age = int(age)

#Determine the ticket price.
    if age < 3:
        print("Your ticket is free.")

    elif age < 13:
        print("Your ticket is $10.")

    else:
        print("Your ticket is $15.")
