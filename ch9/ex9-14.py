# Dice: The module random contains functions that generate random numbers in a
# variety of ways. The function randint() returns an integer in the range you
# provide. The following code returns a number between 1 and 6.
#
# ----------------------------------------------------------------------------
# from random import randint
# x = randint(1, 6)
# ----------------------------------------------------------------------------
#
# Make a class Die with one attribute called sides, which has a default value
# of 6. Write a method called roll_die() that prints a random number between 1
# and the number of sides the die has. Make a 6-sided die and roll it 10
# times.
#
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die():
    def __init__(self, sides):
        if sides >= 2:
            self.sides = sides
        else:
            print("Every story has at least two sides to it!")

    def roll_die(self):
        val = randint(1, self.sides)
        print("You rolled a " + str(val) + " on your " + str(self.sides) + "-sided die.")

die6 = Die(6)
die10 = Die(10)
die20 = Die(20)
for i in range(10):
    die6.roll_die()
print()
for i in range(10):
    die10.roll_die()
print()
for i in range(10):
    die20.roll_die()

