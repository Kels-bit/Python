#Create a list of people to invite to dinner
guests = ['rocky nuggets', 'bailey kings', 'raymond rays', 'steely mcbeam', 'nordy wild' ]

#Remove the guest who cannot make the dinner party
noshow = guests.pop(1)
print(f"{noshow.title()}, has informed us he cannot make the dinner this week")

#Add the new guest to the list.
guests.insert(1, 'henny huges')

print(f"Good day {guests[0].title()}, would you like to join me for dinner this week?")
print(f"Good day {guests[1].title()}, would you like to join me for dinner this week?")
print(f"Good day {guests[2].title()}, would you like to join me for dinner this week?")
print(f"Good day {guests[3].title()}, would you like to join me for dinner this week?")
print(f"Good day {guests[4].title()}, would you like to join me for dinner this week?")
