# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a
# class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 or Exercise 9-4. Either version of the class will work; just
# pick the one you like better. Add an attribute called flavors that stores a
# list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant():
    """A simple restaurant model"""


    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


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


class IceCreamStand(Restaurant):
    """An Ice Cream Stand is a special kind of restaurant."""


    def __init__(self, restaurant_name, cuisine_type, flavors):
        """
        Initialize restaurant_name, cuisine_type and flavors attributes
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors


    def display_flavors(self):
        print(self.flavors)


icecreamstand = IceCreamStand("Hairy Queen", "Ice Cream Stand", ['Vanilla', 'Chocolate', 'Strawberry', 'Butter Pecan'])
icecreamstand.display_flavors()

