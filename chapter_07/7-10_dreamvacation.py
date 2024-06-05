#In this exercise write a program that polls users about their dream vacation.
dream_locations = {}

#Create a Prompt
prompt = f"If you could visit one place in the world,where would you go? "
name_prompt = f'\nWhat is your name? '
repeat_prompt = f"Would you like another person to respond? (yes/no) "
ask_active = True

while ask_active:
    #Prompt the user.
    name = input(name_prompt)
    dream_location = input(prompt)

    #Store in dictionary
    dream_locations[name] = dream_location

    #Prompt for another user or exit
    repeat = input(repeat_prompt)
    if repeat == 'no':
        ask_active = False
        print("\n")
    #Show results of poll.

for name , location in dream_locations.items():
    print(f"{name.title()}'s dream trip is to visit {location.title()}.")

