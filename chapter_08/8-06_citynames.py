""" Write a function called city_country() that takes in the name
of a city and its country. """

#Create function
def city_country(cityStr,countryStr):
    formatted_text = f"{cityStr.title()}, {countryStr.title()}"
    return formatted_text

for_name = city_country('paris', 'france')
for_name0 = city_country('santiago', 'chile')
for_name1 = city_country('los angeles', 'usa')
print("\n")
print(for_name)
print(for_name0)
print(for_name1)

