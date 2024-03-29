# Polling: Use the code in favorite_languages.py (p. 104).

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

## Make a list of people who should take the favorite languages poll. Include
##    some names that are already in the dictionary and some that are not.
to_poll = [ 'kevin', 'tom', 'glen', 'phil', 'edward' ]

## Loop through the list of people who should take the poll. If they have
##    already taken the poll, print a message thanking them for responding. If
##    they have not taken the poll, print a message inviting them to take the
##    poll.
for person in to_poll:
    if person in favorite_languages.keys():
        print('Thanks for responding, ' + person.title() + '!')
    else:
        print('Please take the poll, ' + person.title() + '.')
