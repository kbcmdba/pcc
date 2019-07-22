# Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
## Write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.
## Write one version of the program that passes the if test and another that fails. (The version that fails will have no output)

def get_points(color):
    if (color == 'green'):
        print("You just earned 5 points.")

alien_color='yellow'
print('Expect no output here.')
get_points(alien_color)
print('Expect no output here.')
get_points('red')
print('Expect output here.')
get_points('green')

