# City, Country: Write a function that accepts two parameters: a city name and
# a country name. THe function should return a single string in the form of
# City, Country, such as Santiago, Chile. Store the function in a module
# called city_functions.py
#
def format_city_info(city_name, country_name):
    return f"{city_name}, {country_name}".title()

