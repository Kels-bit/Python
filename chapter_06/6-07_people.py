#Create a dictionary to store information for three people.

person_0 = {'first_name' : 'alexander', 'last_name' : 'hamilton', 'age' : 47, 'city' : 'new york city'}
person_1 = {'first_name' : 'james', 'last_name' : 'madison', 'age' : 85, 'city' : 'montpelier'}
person_2 = {'first_name' : 'john', 'last_name' : 'jay', 'age' : 83, 'city' : 'bedford'}

people = [person_0, person_1, person_2]

for p in people:
    name = f"{p['first_name'].title()} {p['last_name'].title()}"
    age = f"{p['age']}"
    city = p['city'].title()
    print(f"{name}, died at the age of {age} in {city}.")
