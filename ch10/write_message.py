filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I love finding meaning in large data sets.\n")
    file_object.write("I love creating apps that can be run in a browser.\n")
