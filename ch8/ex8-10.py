# Great Magicians: Start with a copy of your program from Exercise 8-9. Write a
# function called make_great() that modifies the list of magicians by adding
# the phrase "the Great" to each magician's name. Call show_magicians() to see
# that the list has actually been modified.

magicians = [ 'Tom', 'Dick', 'Harry' ]

def show_magicians( magicians ):
    for magician in magicians:
        print( magician + ' magically appears.' )

def make_great( mere_magicians ):
    i = 0
    while i < len( mere_magicians ):
        mere_magicians[ i ] = mere_magicians[ i ] + ' the Great'
        i = i + 1

make_great( magicians )
show_magicians( magicians )

