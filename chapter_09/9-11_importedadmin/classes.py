class User:
    """ A class the represents a user's profile."""

    def __init__(self,first_name, last_name, email, username, location):
       self.first = first_name
       self.last = last_name
       self.email = email
       self.username = username
       self.loca = location

    def describe_user(self):
        """ Print information about the user. """
        print(f"\nFirst Name: {self.first.title()}")
        print(f"Last Name: {self.last.title()}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Location: {self.loca.upper()}")

    def greet_user(self):
        print(f"Welcome, {self.first.title()}({self.username})!")

class Admin(User):
    """ Initialize the admin """
    def __init__(self, first_name, last_name, email, username, location):
        super().__init__(first_name, last_name, email, username, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can unban user']

    def show_privileges(self):
        print(f"\nAdmin Privileges")
        print('-------------------\n')
        for priv in self.privileges:
            print(f"- {priv}")
