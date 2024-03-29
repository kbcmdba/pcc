# Checking Usernames: Do the following to create a program that simulates how
# websites ensure that everyone has a unique username.
## Make a list of five or more usernames called current_users.
current_users = ['admin', 'kbenton', 'gpatel', 'sdhingr', 'amaser']

## Make another list of five usernames called new_users. Make sure one or two
## of the usernames are also in the current_users list.
new_users = ['gpatel', 'wwang', 'wwang', 'Amaser', 'mmcdona']

## Loop through the new_users to see if each new username has already been
## used. If it has, print a message that the person will need to enter a new
## username. If a username has not been used, print a message saying that
## the username is available.
## Make sure your comparison is case insensitive. If 'John' has been used,
## 'JOHN' should not be accepted.
for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user.lower() + ', that user name has already been used.')
    else:
        print('Welcome, ' + new_user.lower())
        current_users.append(new_user)
print('The final list of users is...')
print(current_users)

