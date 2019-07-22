from user import User


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


