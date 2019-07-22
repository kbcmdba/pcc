# Magicians: Make a list of magician's names. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
magicians = [ 'Tom', 'Dick', 'Harry' ]

def show_magicians( magicians ):
    for magician in magicians:
        print( magician + ' magically appears.' )

show_magicians( magicians )

