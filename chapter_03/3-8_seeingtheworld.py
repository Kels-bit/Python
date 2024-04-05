#Create a list with places to visted
places = ['korea', 'england', 'japan', 'egypt', 'mexico']

# Print in original order.
print(places)

# Print in alphabetical order
print(sorted(places))

# Print in original order
print(places)

# Print in reverse-alphabetical order without chaning order of original list
print(sorted(places, reverse=True))

# Print orginal order
print(places)

# Print using reverse()
places.reverse()
print(places)

# Print using reverse() to change back
places.reverse()
print(places)

# Print with sort()
places.sort()
print(places)

# Print using sort() to get reverse-alphabetical order.
places.sort(reverse=True)
print(places)
