# Multiples of Ten: Ask the user for a number, and then report whther the number
# is a multiple of 10 or not.

num = input("Please enter a number so I can tell you if it's a multiple of ten: ")
if 0 == int(num) % 10:
    print("That number is a multiple of ten.")
else:
    print("That number is not a multiple of ten.")

