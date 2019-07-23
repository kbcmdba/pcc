# Addition: One common problem when prompting for numerical input occurs when
# people provide text instead of numbers. When you try to convert the input
# to an int, you'll get a ValueError. Write a program that prompts for two
# numbers. Add them together and print the result. Catch the ValueError if
# either input value is not a number, and print a friendly error message.
# Test your program by entering two numbers and then by entering some text
# instead of a number.

string_1 = input("Please enter a number you wish to add: ")
string_2 = input("Please enter another number you wish to add: ")

try:
    sum = int(string_1) + int(string_2)
except ValueError:
    print("Sorry, one or both of those didn't convert to integers.")
else:
    print(f"{string_1} + {string_2} = {sum}")

