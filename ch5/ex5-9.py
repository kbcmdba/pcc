# No Users: Add an if to test hello_admin.py to make sure the list of users is not empty.
## If the list is empty, pring the message We need to find some users!
## Remove all of the usernames from your list, and make sure the correct message is printed.

usernames = ['admin', 'kbenton', 'gpatel', 'sdhingr', 'amaser']

def is_list_empty(list):
    if 0 == len(list):
        print("We need to find some users!")

is_list_empty(usernames)
is_list_empty([])

