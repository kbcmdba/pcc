# Users: Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called desccribe_user that prints a summary
# of the user's information. Make another method called greet_user that prints
# a personalized greeting of the user.
#
# Create several instances representing different users, and call both methods
# for each user.

class User():
    """A rudimentary user class."""

    def __init__(
            self,
            first_name,
            last_name,
            userid,
            password,
            home_directory,
            login_shell):
        """Initialize the object"""
        self.first_name = first_name
        self.last_name = last_name
        self.userid = userid
        self.password = password
        self.home_directory = home_directory
        self.login_shell = login_shell


    def describe_user(self):
        """Describe a user fully."""
        print("\nUser: " + self.userid)
        print("\tFirst Name: " + self.first_name)
        print("\tLast Name: " + self.last_name)
        print("\tPassword: " + self.password)
        print("\tHome Directory: " + self.home_directory)
        print("\tLogin Shell: " + self.login_shell)


    def greet_user(self):
        """Greet the user."""
        print("Hello, " + self.first_name + " " + self.last_name + ".")

users = [ User('Joe', 'Cool', 'jcool', 'Barnstormer', '/home/jcool', '/bin/bash'),
          User('Charlie', 'Brown', 'cbrown', 'Confused', '/home/cbrown', '/bin/bash'),
          User('Lucy', 'van Pelt', 'lvpelt', 'Bully', '/home/lvpelt', '/bin/csh')]

for user in users:
    user.describe_user()
    user.greet_user()

