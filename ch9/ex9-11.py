# Imported Admin: Start with your work from Exercise 9-8. Store the classes,
# User, Privileges, and Admoin in one module. Create a separate file, make
# an Admin instance, and call show_privileges() to show that everything is
# working correctly.

from user import User
from admin import Privileges, Admin

admin = Admin('Joe', 'Cool', 'jcool', 'Barnstormer', '/home/jcool', '/bin/bash', ['can add post', 'can ban user'])
admin.describe_user()
admin.privileges.show_privileges()

