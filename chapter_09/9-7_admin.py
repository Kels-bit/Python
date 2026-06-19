"""An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""


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



   #Create Instances and Output
profile = Admin('mightpython', 'man', 'mrpython@python.com', 'iwillbanyou', 'na')
profile.describe_user()
profile.greet_user()
profile.show_privileges()
