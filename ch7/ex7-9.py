# No Pastrami: Using the list sandiwch_orders from Exercise 7-8, make sure the
# sandwich 'pastrami' appears in the list at least three times. Add code near
# the beginning of your program to print a message saying the deli has run out
# of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in
# finished_sandwiches.
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
print("Sorry, the deli is out of pastrami.")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if 'pastrami' == sandwich:
        continue
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
# finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
print("\nI've made the following sandwiches:\n")
for sandwich in finished_sandwiches:
    print("A " + sandwich + " sandwich")


