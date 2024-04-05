#Create a list of people to invite to dinner
guests = ['rocky nuggets', 'bailey kings', 'raymond rays', 'steely mcbeam', 'nordy wild' ]

#Add new additions to list
#Add at the beginning
guests.insert(0, 'henny huges')

#Add in the middle
guests.insert(3, 'hugo bugs')

#Add at the end
guests.append('grizz bizz')

#Inform guest of your table issue.
print(f"Hello everyone, unfortunately I am having issues with the delivery of my new table and can only invite two guests for dinner this week")

#Inform guest that they are not invited for dinner.
noinvite1 = guests.pop(1)
noinvite2 = guests.pop(1)
noinvite3 = guests.pop(2)
noinvite4 = guests.pop(1)
noinvite5 = guests.pop(1)
noinvite6 = guests.pop(1)

print(f"Hello, {noinvite1.title()}, due to the limited space you are no longer invited to the dinner this week.")
print(f"Hello, {noinvite2.title()}, due to the limited space you are no longer invited to the dinner this week.")
print(f"Hello, {noinvite3.title()}, due to the limited space you are no longer invited to the dinner this week.")
print(f"Hello, {noinvite4.title()}, due to the limited space you are no longer invited to the dinner this week.")
print(f"Hello, {noinvite5.title()}, due to the limited space you are no longer invited to the dinner this week.")
print(f"Hello, {noinvite6.title()}, due to the limited space you are no longer invited to the dinner this week.")

#Guests still invite
print(f"Good day {guests[0].title()}, you are still invited to the dinner this week.")
print(f"Good day {guests[1].title()}, you are still invited to the dinner this week.")
