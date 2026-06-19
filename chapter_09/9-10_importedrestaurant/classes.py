""" This module contains the classes used for this program."""


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

