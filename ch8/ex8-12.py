# Sandwiches: Write a function that accepts a list of items a person wants on a
# sandwich. The function should have one parameter that collects as many items
# as the function provides, and it should print a summary of the sandwich that
# is being ordered. Call the function three times, using a different number of
# arguments each time.

def make_sandwich( *items ):
    for item in items:
        print( "Adding " + item + " to your sandwich." )

make_sandwich('turkey', 'cheese', 'mayo', 'tomato')
make_sandwich('roast beef', 'brown mustard')
make_sandwich('bacon', 'lettuce', 'tomato')

