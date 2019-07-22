# City Names: Write a function called city_country() that takes in the name of
# a city and its country. The function should return a string formatted like
# this "Santiago, Chile"
#
# Call your function with at least three city-country pairs, and print the value
# that's returned.

def city_country(city, country):
    return(city + ", " + country)

print(city_country('London', 'England'))
print(city_country('Paris', 'France'))
print(city_country('Moscow', 'Russia'))

