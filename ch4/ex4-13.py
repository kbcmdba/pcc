# A buffet-style reastaurant offers only five basic foods. Think of five simple foods, and store them as a tuple.
foods = ('Chicken', 'Corn', 'Beans', 'Rice', 'Salad')
## Use a for loop to print each food the restaurant offers
print("Yesterday's Restaurant Menu:")
for food in foods:
	print(food)
## Try to modify one of the items and make sure that Python rejects the change
# INVALID CODE:
# foods[1] = 'Apple'
## The restaurant changes its menu, replacing two if the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

foods = ('Beef', 'Potatoes', 'Beans', 'Rice', 'Salad')
print("Today's Restaurant Menu:")
for food in foods:
	print(food)

