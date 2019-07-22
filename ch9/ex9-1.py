# Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant that prints a message
# indicating that hte restaurant is open.
#
# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.

class Restaurant():
    """A simple restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant attributes"""
        print(self.restaurant_name + " serves " + self.cuisine_type + ".")

    def open_restaurant(self):
        """Really?"""
        print(self.restaurant_name + " is now open.")

one_restaurant = Restaurant("Joe's", "greasy seafood")
one_restaurant.describe_restaurant()
one_restaurant.open_restaurant()

