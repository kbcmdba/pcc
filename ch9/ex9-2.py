# Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

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

restaurant_one = Restaurant("Joe's", "greasy seafood")
restaurant_one.describe_restaurant()
restaurant_one = Restaurant("Taco Bell", "greasy mexican")
restaurant_one.describe_restaurant()
restaurant_one = Restaurant("Silver Lake", "chinese")
restaurant_one.describe_restaurant()

