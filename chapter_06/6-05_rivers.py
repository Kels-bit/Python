#Create a dictionary containing major rivers and the countryeach runs through.
rivers = { 
          'amazon' : 'brazil',
          'nile' : 'egypt',
          'ganges' : 'india',
          'mississippi' : 'usa',
          }

#Use a loop to print a sentence about each river.
for r, c in rivers.items():
    if c == 'usa':
        print(f"\nThe {r.title()} river runs through the USA.")
    else:
        print(f"\nThe {r.title()} river runs through {c.title()}.")
#Use a loop to print each river in the dictionary.
print(f"\nEach river included in the dictionary:")
for r in rivers.keys():
    print(f"\t{r.title()}")
#Use a loop to print each name of each country in the dictionary.
print(f"\nEach country included in the dictionary:")
for c in rivers.values():
    if c == 'usa':
        print('\tUSA')
    else:
        print(f"\t{c.title()}")

