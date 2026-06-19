"""Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance. """


class Restaurant:
    """ A class to model a restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Describes two things about the restaurant. """
        print(f"\nRestaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type : {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")


food1 = Restaurant("wendy's", 'fast food')
food2 = Restaurant("lucille's smokehouse", 'bar-b-que')
food3 = Restaurant('wingstop', 'wings fries, and sides')                  

#Call instance 1
food1.describe_restaurant()
food1.open_restaurant()

#Call instance 2
food2.describe_restaurant()
food2.open_restaurant()

#Call instance 3
food3.describe_restaurant()
food3.open_restaurant()
