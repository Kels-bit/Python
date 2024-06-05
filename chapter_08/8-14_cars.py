"""Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. """

def make_car(make, model , **options):
    car_dict = {
            'make' : make,
            'model' : model,
            }
    for o, v, in options.items():
        car_dict[o] = v


    return car_dict

outback = make_car('subaru', 'outback', color='blue', tow_package=True)

challenger = make_car('dodge', 'challenger', color='gray', transmission='auto', tire='old')

soul = make_car('kia', 'soul', transmission='manual', seats='leather', doors=4)

print(outback)
print(challenger)
print(soul)
