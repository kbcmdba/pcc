# Deli: Make a list called sandwich_orders and fill it with names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
sandwich_orders = [ 'pastrami'
                  , 'tuna'
                  , 'bologana'
                  , 'BLT'
                  , 'salami'
                  , 'tuna'
                  , 'pastrami'
                  , 'cheese'
                  , 'tomato'
                  , 'BLT'
                  , 'tuna'
                  , 'chicken'
                  , 'roast beef'
                  , 'pastrami' 
                  ]
finished_sandwiches = []
# the list of sandwich_orders and print a message for each order, such as I
# made your tuna sandwich. As each sandwich is made, move it to the list of
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
# finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
print("\nI've made the following sandwiches:\n")
for sandwich in finished_sandwiches:
    print("A " + sandwich + " sandwich")


