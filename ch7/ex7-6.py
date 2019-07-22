# Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
## Use a conditional test in the while statement to stop the loop.
## Use an action variable to control how long the loop runs.
## Use a break statement to exit the loop when the user enters a 'quit' value.

action = 0
while action < 3:
    action = action + 1
    print("Enter a topping to add to your pizza.")
    print("Enter the word quit by itself to stop adding toppings.")
    topping = input(": ")
    if "quit" == topping:
        break;
    print("I'll add " + topping + " to your pizza.")
    print("\n")

