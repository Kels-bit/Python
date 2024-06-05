#Create a dictonary to store people's favorite numbers.
favorite_numbers = {
        'kelsey' : [18],
        'mia' : [1, 2, 3, 4, 5],
        'taj' : [7, 8, 9],
        'misha' : [11, 22, 33, 44, 55, 66, 77],
        'desmond' : [19, 21],
        }

#Print each key and value in the dictonary.
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

