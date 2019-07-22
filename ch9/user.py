
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


