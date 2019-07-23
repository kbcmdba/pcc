# Favorite Number: Write a program that prompts for the user's favorite
# number. Use json.dump() to store this number in a file. Write a separate
# program that reads in this value and prints the message, "I know your
# favorite number is ___."

from json import dump

filename = 'favorite_number.json'
number = input('What is your favorite number? ')
try:
    n = float(number)
except ValueError:
    print("Sorry - that's not a number.")
else:
    with open(filename, 'w') as file_object:
        dump(n, file_object)

