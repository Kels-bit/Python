#Create a list for the dictonaries.
pets = []

#Create the dictionaries
pet_0 = {
    'name' : 'jello',
    'color': 'yellow',
    'owner': 'joe',
        }
pets.append(pet_0)

pet_1 = {
    'name' : 'shane jr',
    'color' : 'blue',
    'owner' : 'shane',
        }
pets.append(pet_1)

pet_2 = {
    'name' : 'moon',
    'color' : 'white',
    'owner' : 'pew',    
        }
pets.append(pet_2)

pet_3 = {
    'name' : 'rook',
    'color' : 'brown',
    'owner' : 'joe',
        } 
pets.append(pet_3)

for p in pets:
    print('\n')
    for key,value in p.items():
        print(f"\t{key}:{value}")
        
