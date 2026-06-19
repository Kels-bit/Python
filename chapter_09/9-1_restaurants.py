"""Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods. """


class Restaurant:
    """ A class to model a restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Describes two things about the restaurant. """
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type : {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")


food = Restaurant("wendy's", 'fast food')

food.describe_restaurant()
food.open_restaurant()
