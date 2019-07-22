# You don't have to limit the number of tests you create to 10. If you
#    want to try more compairisons, write more tests and add them to
#    condidtional_tests.py. Have at least one True and one False result
#    for each of the following:
## Tests for equality and inequality with strings
a = 'a'
b = 'b'
print("if (a == b); Expect false")
if (a == b):
    print("Should never get here.")
if (a != b):
    print("This is the expected response: a != b")
## Tests using the lower() function
print("if (a.upper() == a.lower()): Expect false")
if (a.upper() == a.lower()):
    print("Should never get here either.")
if (a.upper() != a.lower()):
    print("This is the expected response: a.upper() != a.lower()")
## Numerical tests involving equality and inequality, greater than and
##    less than, greater than or equal to, and less than or equal to
x = 1
y = 2
print("if (x == y): Expect false")
if (x == y):
    print("Should also never get here.")
if (x != y):
    print("This is the expected response: x != y")
print("if (x < y): Expect true")
if (x < y):
    print("This is the expected response: x < y")
if (x > y):
    print("Should never get here with x > y")
print("if (x <= y): Expect true")
if (x <= y):
    print("This is the expected response: x <= y")
if (x >= y):
    print("Should never get here with x >= y")
## Tests using the and keyword and the or keyword
print("if (a != b) and (x < y): Expect true")
if (a != b) and (x < y):
    print("a != b and x < y is true.")
print("if (a == b) or (x < y): Expect true")
if (a == b) or (x < y):
    print("As expected again.")

## Tests whether an item is in a list
my_list = ('a', 'b', 'c')
print('a is in my_list: expect true')
if ('a' in my_list):
    print("And so it is.")

## Tests whether an item is not in a list
print('z is not in my_list: expect true')
if ('z' not in my_list):
    print("And so it isn't.")

