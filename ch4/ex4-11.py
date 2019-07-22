# My Pizzas, Your Pizzas: Start your program from exercise 4-1. Make a copy of the list of pizzas and call it friend pizzas. Then do the following:
## Add a new pizza to the original list.
## Add a different pizza to the list friend_pizzas.
## Prove that you have two separate lists. Print the message, My favorite pizzas are:, and then use a for loop to print the first list. Print the message, My Friend's foavrite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

pizzas = [ "Cheese", "Pepperoni", "Sausage" ]
friend_pizzas = pizzas[:]
pizzas.append('Tomato')
friend_pizzas.append('Artichoke Hearts')
for pizza in pizzas:
	print("I really like " + pizza + " pizza.")
for pizza in friend_pizzas:
	print("My friend really likes " + pizza + " pizza.")
print("Can't you see that we really love pizza?")

