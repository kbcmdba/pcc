# Pizza Toppings: Write a loop that prompts the user to enter a series of pizza
# toppings until they enter a 'quit' value. As they enter each topping, print a
# message saying you'll add that topping to their pizza.

while True:
    print("Enter a topping to add to your pizza.")
    print("Enter the word quit by itself to stop adding toppings.")
    topping = input(": ")
    if "quit" == topping:
        break;
    print("I'll add " + topping + " to your pizza.")
    print("\n")

