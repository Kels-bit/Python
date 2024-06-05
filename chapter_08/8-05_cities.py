""" Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country. """


def describe_city(city, country = 'earth'):
    if country == 'earth':
        print(f"{city.title()} is on Earth.")
    else:
        print(f"{city.title()} is in {country.title()}.")
    

describe_city('paris', 'france')
describe_city('seoul', 'south korea')
describe_city('los angeles')
