# Imported Restaurant: Using your latest Restaurant class, store it in a
# module.Make a separate file that imports Restaurant. Make a Restaurant
# instance and call one of Restaurant's methods to show tha tthe import
# statement is working properly.

from restaurant import Restaurant

my_restaurant = Restaurant('Red Lobster', 'Seafood')
my_restaurant.describe_restaurant()

