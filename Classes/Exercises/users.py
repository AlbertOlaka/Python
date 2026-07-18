class User:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0

    def describe_user(self):
        """Describing the user."""
        print(f"The users name is {self.first_name} {self.last_name}.")
        print(f"The users email is {self.email}")
        print(f"The users phone number is {self.phone_number}")

    def greet_user(self):
        """greeting the user!"""
        print(f"Hello {self.first_name} {self.last_name}!")

    def read_login(self):
        """Print a statement showing the users login attempts."""
        print(f"{self.first_name} {self.last_name} has attempted to login {self.login_attempts}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reseting login attempts to zero."""
        self.login_attempts = 0

class Privileges:
    """A simple attemp to model privileges for admin."""

class Admin(User):
    def __init__(self, first_name, last_name, email, phone_number, privileges):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, email, phone_number)
        self.privileges = privileges

    def show_priveleges(self):
        """Print a statement displaying the admins privileges."""
        for privilege in self.privileges:
            print(f"- {privilege}")

user = User('Willie', 'John', 'wjohn@gmail.com', 123456)
user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.read_login()

user.reset_login_attempts()
user.read_login()

user.read_login()


user_1 = Admin ('Lucy', 'Jow', 'ljow@gmail.com', 987655, ['can add post', 'can delete post', 'can ban user'])
user_1.describe_user()
user_1.show_priveleges()
user_1.greet_user()

# user_2 = User('Jane', 'Joe', 'jj@gmail.com', 876554)
# user_2.describe_user()
# user_2.greet_user()

# user_3 = User('John', 'Doe', 'jdoe@gmail.com', 456781)
# user_3.describe_user()
# user_3.greet_user()