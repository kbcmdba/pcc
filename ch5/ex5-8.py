# Hello Admin: Make a list o five or more usernames, including the name
#'admin'. Imagine you are writing code that will print a greeting to each
# user after they log in to a website. Loop through the list, and print a
# greeting to each user:
usernames = ['admin', 'kbenton', 'gpatel', 'sdhingr', 'amaser']

def print_greeting(username):
    ## If the username is 'admin', print a special greeting such as Hello
    ##   admin, would you like to see a status report?
    if username == 'admin':
        print('Hello admin. Would you like to see a status report?')
    ## Otherwise, print a generic greeting, such as Hello Eric thank you for
    ##    logging in again.
    else:
        print('Hello ' + username + '. Thank you for logging in again.')

for username in usernames:
    print_greeting(username)

