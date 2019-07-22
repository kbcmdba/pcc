# Login Attempts: Add an attribute called login_attempts to your User class
# from Exercise 9-3. Write a method called increment_login_attempts() that
# increments the value of login attempts by 1. Write another method called
# reset_login_attempts() that resets the value of login_attempts to 0.
#
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_atttempts to make sure it was
# incremented properly, and then call reset_login-attempts(). Print
# login_attempts again to make sure it was reset to 0.

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
        self.login_attempts = 0


    def describe_user(self):
        """Describe a user fully."""
        print("\nUser: " + self.userid)
        print("\tFirst Name: " + self.first_name)
        print("\tLast Name: " + self.last_name)
        print("\tPassword: " + self.password)
        print("\tHome Directory: " + self.home_directory)
        print("\tLogin Shell: " + self.login_shell)
        print("\tLogin Attempts: " + str(self.login_attempts))


    def greet_user(self):
        """Greet the user."""
        print("Hello, " + self.first_name + " " + self.last_name + ".")


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


users = [ User('Joe', 'Cool', 'jcool', 'Barnstormer', '/home/jcool', '/bin/bash'),
          User('Charlie', 'Brown', 'cbrown', 'Confused', '/home/cbrown', '/bin/bash'),
          User('Lucy', 'van Pelt', 'lvpelt', 'Bully', '/home/lvpelt', '/bin/csh')]


for user in users:
    user.describe_user()
    user.greet_user()
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.describe_user()
    user.reset_login_attempts()
    user.describe_user()

