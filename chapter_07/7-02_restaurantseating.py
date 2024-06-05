dinner_group = input('How many people are in your dinner group? ')
dinner_group = int(dinner_group)
if dinner_group > 8:
    print('There is a wait time for your group size.')
else:
    print("Your table is ready. Right this way.")
