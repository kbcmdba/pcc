# Number Served: Start with your program from exercise 9-1. Add an attribute
# called number_served with a default value of 0. Create an instance called
# restaurant from this class. Print the number of customers the restaurant has
# served, and then change its value and print it again.
#
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and
# print the value again.
#
# Add a method called increment_number_served() that lets you increment the
# number of customers who've been served. Call this method with any number you
# like that could represent how many customers were served, in say, a day of
# business.

class Restaurant():
    """A simple restaurant model"""


    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served


    def describe_restaurant(self):
        """Print the restaurant attributes"""
        print(self.restaurant_name +
                " has served " +
                str(self.number_served) +
                " customers " +
                self.cuisine_type +
                ".")


    def open_restaurant(self):
        """Really?"""
        print(self.restaurant_name + " is now open.")


    def set_number_served(self, number_served):
        """Setter"""
        self.number_served = number_served


    def increment_number_served(self, increment_by):
        """Modifier"""
        self.number_served += increment_by


restaurant_one = Restaurant("Joe's", "greasy seafood")
restaurant_one.describe_restaurant()
restaurant_one.number_served = 79
restaurant_one.describe_restaurant()
restaurant_one.set_number_served(184)
restaurant_one.describe_restaurant()
restaurant_one.increment_number_served(120)
restaurant_one.describe_restaurant()

