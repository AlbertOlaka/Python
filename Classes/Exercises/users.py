class User:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
    def describe_user(self):
        print(f"The users name is {self.first_name} {self.last_name}.")
        print(f"The users email is {self.email}")
        print(f"The users phone number is {self.phone_number}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

user = User('Willie', 'John', 'wjohn@gmail.com', 123456)
user.describe_user()
user.greet_user()

user_1 = User('Lucy', 'Jow', 'ljow@gmail.com', 987655)
user_1.describe_user()
user_1.greet_user()

user_2 = User('Jane', 'Joe', 'jj@gmail.com', 876554)
user_2.describe_user()
user_2.greet_user()

user_3 = User('John', 'Doe', 'jdoe@gmail.com', 456781)
user_3.describe_user()
user_3.greet_user()