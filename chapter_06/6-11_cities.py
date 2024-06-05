#Create a dictionary
cities = {
        'los angeles' : {
            'country' : 'usa',
            'population' : 3748640,
            'fact' : "The film industry moved to LA to flee Thomas Edison's patents."
            },

        'london' : {
            'country' : 'uk',
            'population' : 12434823,
            'fact' : "There is belief that the Tower of London will fall if at least six raven aren't in residence at any given time."
            },

        'paris' : {
        'country' : 'france',
        'population' : 13115000,
        'fact' :  'Paris has five Statues Of Liberty.'
            }
        }

for city, city_info in cities.items():
    print(f"\nCity Name: {city.title()}")
    if city_info['country'] == 'usa':
        country = 'USA'
    elif city_info['country'] == 'uk':
        country = 'UK'
    else:
        country = city_info['country']

    poplevel = f"{city_info['population']}"
    cityfact = f"{city_info['fact']}"

    print(f"Country: {country}")
    print(f"Population: {poplevel}")
    print(f"Fact: {cityfact}")

