# Favorite Number Remembered: Combine the two programs from Exercise 10-11
# into one file. If the number is already stored, report the favorite number
# to the user. If not, prompt for the user's favorite number and store it
# in a file. Run the program twice to see that it works.

from json import dump, load

filename = 'favorite_number12.json'
try:
    with open(filename, 'r') as file_object:
        number = load(file_object)
    print(f"I know your favorite number is {number}.")
except FileNotFoundError:
    number = input('What is your favorite number? ')
    try:
        n = float(number)
    except ValueError:
        print("Sorry - that's not a number.")
    else:
        with open(filename, 'w') as file_object:
            dump(n, file_object)
            print("Thanks - I'll remember that for next time.")

