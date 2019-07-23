# Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt

name = input("Hello, guest. Please enter your name: ")
with open('guest.txt', 'a') as file_object:
    file_object.write(name + '\n')
