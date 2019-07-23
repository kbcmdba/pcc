# Favorite Number: Write a program that prompts for the user's favorite
# number. Use json.dump() to store this number in a file. Write a separate
# program that reads in this value and prints the message, "I know your
# favorite number is ___."

from json import load

filename = 'favorite_number.json'
try:
    with open(filename, 'r') as file_object:
        number = load(file_object)
    print(f"I know your favorite number is {number}.")
except FileNotFoundError:
    print("Did you tell me what your favorite number is? I don't seem to be able to find it.")

