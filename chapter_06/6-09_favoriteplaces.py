#Create a dictionary
favorite_places = {
    'kelsey' : ['dallas', 'carolina'],
    'taj' : ['india', 'spain','france', 'south korea'],
    'desmond' : [ 'home', 'work', 'car']
        }

for name, places in favorite_places.items():
    print(f"\n{name.title()} favorite places are:")
    for p in places:
        print(f"{p.title()}")
