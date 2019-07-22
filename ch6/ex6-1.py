# Person: Use a dictionary to store information about a person you know. Store
# their first name, last name, age, and city. Print each piece of inromation
# stored in your dictionary.

person = { "first_name": "Dave", "last_name": "Nelson", "age": 52, "city": "Tallmadge" }
for key, value in person.items():
    print(str(key) + ' is ' + str(value))

