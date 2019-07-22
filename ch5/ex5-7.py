# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

## Make a list of your three favorite fruits and call it favorite_fruits.
favorite_fruits = ['apples', 'banannas', 'kiwi']
def check_fruit(yes_or_no, fruit):
    print('Are ' + fruit + ' on my favorite fruit list? ' + yes_or_no + '.')
    if fruit in favorite_fruits:
        print('You really like ' + fruit + '!')
    if fruit not in favorite_fruits:
        print('Not so much.')

## Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as "You really like banannas!"
check_fruit('No', 'oranges')
check_fruit('Yes', 'kiwi')
check_fruit('Yes', 'apples')
check_fruit('No', 'grapefruit')
check_fruit('Yes', 'banannas')

