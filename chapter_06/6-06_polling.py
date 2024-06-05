favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
     }

# Make a list of people who should take the favorite languages poll. 
# Includesome names of people that are already in the list and some who are not.
pollers = ['jen', 'sarah', 'dirk', 'luka', 'bryce']

#Loop through the list. If they have taken the poll thank them.
#If they haven't taken the poll invite them to take the poll.

for name in pollers:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()}, for responding to the poll.")
    else:
        print(f"Hello, {name.title()}. We noticed you have not repsonded to the poll, please respond at your earliest convenience.")
