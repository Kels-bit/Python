"""Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.
"""

class Restaurant:
    """ A class to model a restaurant. """

    def __init__(self, restaurant_name, cuisine_type):
        """ Initialize name and age attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Describes two things about the restaurant. """
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type : {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")
    
    def n_served(self):
        """ Prints the number of customers the restaurant has served. """
        print(f"This restaurant has served {self.number_served} customers.")

    def set_number_served(self, meals):
        """ Sets the number of served """
        self.number_served = meals
    
    def increment_number_served(self,meals):
        """ Increments the customers served. """
        self.number_served += meals


food = Restaurant("wendy's", 'fast food')

food.n_served()
food.number_served = 25
food.n_served()

food.set_number_served(200)
food.n_served()
food.increment_number_served(500)
food.n_served()
