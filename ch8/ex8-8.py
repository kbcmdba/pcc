# User Albums: Start with your program from Exercisek 8-7. Write a while loop
# that allows users to enter an album's artist and title. Once you have the
# information, call make_album() with the user's input and print the
# dictionary that's created. Be sure to include a quit valve in the while loop.

def make_album( name, title, tracks = 0 ):
    album_info = { 'name': name, 'title': title }
    if tracks:
        album_info['tracks'] = tracks
    return album_info

while True:
    print('Please tell me about an album.')
    print('Enter \'q\' at any time to stop.')
    title = input('Album Title: ')
    if 'q' == title:
        break
    artist = input('Album Artist: ')
    if 'q' == artist:
        break
    print(make_album( artist, title ))

