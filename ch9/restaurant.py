
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


