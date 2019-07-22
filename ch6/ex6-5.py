# Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
rivers = { 'nile': 'egypt', 'euphrates': 'egypt', 'rhine': 'germany', 'amazon': 'brazil'}
## Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title() + '.' )
## Use a loop to print the name of each river included in the dictionary.
for river in sorted(rivers.keys()):
    print('The ' + river.title() + ' is a river.')
## Use a loop to print the name of each country included in the dictionary.
for country in sorted(rivers.values()):
    print( country.title() + ' is a country.')

