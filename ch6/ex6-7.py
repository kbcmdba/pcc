# People: Start with the program you wrote for exercise 6-1. Make two new
# dictionaries representing different people, and store all three dictionaries
# in a list called people. Loop through your list of people. As you loop
# through the list, print everything you know about each person.

person = { "first_name": "Dave", "last_name": "Nelson", "age": 52, "city": "Tallmadge" }
for key, value in person.items():
    print(str(key) + ' is ' + str(value))
print("\n")
people = [ person,
           { "first_name": "Dave", "last_name": "Kester", "age": 60, "city": "Akron" },
           { "first_name": "Bob", "last_name": "McNutt", "age": 53, "city": "Akron" }
         ]

for person in people:
    for key, value in person.items():
        print(str(key) + ' is ' + str(value))
    print("")

