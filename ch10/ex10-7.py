# Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so
# the user an continue entering numbers even if they mnake a nistake and
# enter text instead of a number.


converted = False
while False == converted:

    string_1 = input("Please enter a number you wish to add: ")
    string_2 = input("Please enter another number you wish to add: ")

    try:
        sum = int(string_1) + int(string_2)
    except ValueError:
        print("Sorry, one or both of those didn't convert to integers. Please try again.")
    else:
        print(f"{string_1} + {string_2} = {sum}")
        converted = True

