# Privileges: Write a separate Privileges class. This class should have one
# attribute, privileges, that stores a list of strings as described in
# Exercise 9-7. Move the show_privileges() method to this class. Make a
# Privileges instance as an attribute in the Admin class. Create a new
# instance of Admin and use your method to show its privileges.

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


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges


    def show_privileges(self):
        print("This user has the following privileges:")
        print(self.privileges)



class Admin(User):
    def __init__(
            self,
            first_name,
            last_name,
            userid,
            password,
            home_directory,
            login_shell,
            privileges):
        """Initialize the object"""
        super().__init__(
                first_name,
                last_name,
                userid,
                password,
                home_directory,
                login_shell)
        self.privileges = Privileges(privileges)


admin = Admin('Joe', 'Cool', 'jcool', 'Barnstormer', '/home/jcool', '/bin/bash', ['can add post', 'can ban user'])
admin.describe_user()
admin.privileges.show_privileges()
