# Favorite Numbers: Use a dictionary to store people's favorite numbers. Think
# of five names, and se them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person's name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favorite_numbers = {'Rhea': 6, 'KB': 3, 'Mark': 42, 'Ravi': 17, 'Mitra': 0}
for name, num in favorite_numbers.items():
    print(name + "'s favorite number is: " + str(num))

