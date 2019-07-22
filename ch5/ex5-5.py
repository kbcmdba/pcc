# Turn your if-else chain from Exercise 5-4 into an ifl-elif-else-chain.
## If the alien is green, print a message that the player earned 5 points.
## If the alien is yellow, print a message that the player earned 10 points.
## If the alien is red, print a message that the player earned 15 points.
## Write three versions of this program, making sure each message is printed for the appropriate color alien.

def get_points(color):
    if (color == 'green'):
        print("You just earned 5 points.")
    elif (color == 'yellow'):
        print("You just earned 10 points.")
    else:
        print("You just earned 15 points.")

alien_color='yellow'
print('Expect output here.')
get_points(alien_color)
print('Expect output here.')
get_points('red')
print('Expect output here.')
get_points('green')

