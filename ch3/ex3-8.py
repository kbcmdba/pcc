# Store five locations in a lists not in alphabetical order.
places = ['Grand Canyon', 'Old Faithful', 'Eiffel Tower', 'Freedom Tower', 'Dog Park']

# Print the list in its original order
print(places)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(places))

# Show that your list is still in its original order by printing it again
print(places)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print(places)

# Use reverse to change the order of your list again. Print the list to show it's back in its original order.
places.reverse()
print(places)

# Use sort() to change your list so it's sorted in alphabetical order. Print the list to show that its order has changed.
places.sort()
print(places)

# Use sort() to change your list so it's sotored in reverse alphabetical order. Print the list to show that its order has changed.
places.sort(reverse=True)
print(places)
