# OrderedDict Rewrite: Start with Exercise 6-4, where you used a standard
# dictionary to represent a glossary. Rewrite the program using the
# OrderedDict class and make sure the order of the output matches the order in
# which the key-value pairs were added to the dictionary.

from collections import OrderedDict

glossary = {} # OrderedDict()

glossary['List'] = 'A list of primitives or objects'
glossary['Dictionary']='Glossary'
glossary['Key-Value Pairs']='Pairs of keys and the associated values in a dictionary.'

for key, value in glossary.items():
    print("\nItem: " + key + "\nDefinition: " + value)

