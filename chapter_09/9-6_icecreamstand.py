"""An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method. """

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

class IceCreamStand(Restaurant):
        """ Models a ice cream stand """
        def __init__(self,restaurant_name,cuisine_type):
            super().__init__(restaurant_name,cuisine_type)
            self.flavor_types = ['vanilla', 'chocalate', 'strawberry']
        
        def list_flavors(self):
            print(f"\nFlavors")
            print(f"___________")
            for flavor in self.flavor_types:
                print(f"- {flavor.title()}")

icecream = IceCreamStand('cold stone', 'ice cream')

icecream.describe_restaurant()
icecream.list_flavors()
