"""A class describing users."""
class Users:
    """An attempt to know and welcome new users."""

    def __init__(self,first_name, last_name,user_name, age,email):
        """Initialize users' basic attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age
        self.email = email
        self.login_attempts = 0
        #self.email = f"{self.first_name}{self.last_name}@example.com"


    def describe_user(self):
        """Describing user based on user info."""
        print(f"\n{self.user_name}:"
              f"\n\tFirst name {self.first_name}"
              f"\n\t Last name:{self.last_name}"
              f"\n\t Age:{self.age}"
              f"\n\t Email:{self.email}")
        # print(f"\n\t Email:{self.email}")

    def greet_user(self):
        """A simple greetingwel/come message to the user."""
        print(f"\nHello {self.first_name}! we are happy to have you here.")

    def increment_login_attempts(self, attempts):
        """Tell how many times the user has tried to login"""
        self.login_attempts += attempts
        print(f"You have attempted to login {self.login_attempts} times")
