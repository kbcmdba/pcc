# Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians' names. Because the
# original list will be unchanged, return the new list and store it in a
# separate list. Call show_magicians() with each list to show that you have one
# list of the original names and one list with the Great added to each
# magician's name.

mere_magicians = [ 'Tom', 'Dick', 'Harry' ]

def show_magicians( magicians ):
    for magician in magicians:
        print( magician + ' magically appears.' )

def make_great( mere_magicians ):
    i = 0
    while i < len( mere_magicians ):
        mere_magicians[ i ] = mere_magicians[ i ] + ' the Great'
        i = i + 1
    return mere_magicians

great_magicians = make_great( mere_magicians[:] )
print("Expect to see mere magicians here.")
show_magicians( mere_magicians )
print("Expect to see great magicians here.")
show_magicians( great_magicians )

