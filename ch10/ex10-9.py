# Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename, 'r') as file_object:
            print(file_object.read())
    except FileNotFoundError:
        pass

