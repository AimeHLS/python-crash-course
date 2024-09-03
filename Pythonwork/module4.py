"""Multiple classes to describe users."""

from module5 import Users

class Privileges:
    """Indicate admin's privileges among users."""

    def __init__(self,privilege):
        """Initialize attribute"""
        self.privileges = privilege

    def show_privileges(self):
        """Indicating privileges enjoyed by admin"""
        print("\nAs an admin, you can do the following things:")
        for priv in self.privileges:
            print("." + priv.title())



class Admin(Users):
    """"Describing an admin as a special case for users class"""

    def __init__(self,first_name, last_name,user_name, age,email, privilege):
        """
        Initializing attributes for parent class.
        Adding new attributes for child class.
        """
        super(). __init__(first_name, last_name, user_name, age, email)
        self.privileges = Privileges(privilege)