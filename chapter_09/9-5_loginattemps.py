""" Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0. """


class User:
    """ A class the represents a user's profile."""

    def __init__(self,first_name, last_name, email, username, location):
       self.first = first_name
       self.last = last_name
       self.email = email
       self.username = username
       self.loca = location
       self.login_attempts = 0
       
    def describe_user(self):
        """ Print information about the user. """
        print(f"\nFirst Name: {self.first.title()}")
        print(f"Last Name: {self.last.title()}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Location: {self.loca.upper()}")
        
    def greet_user(self):
        print(f"Welcome, {self.first.title()}({self.username})!")

    def increment_login_attempts (self): 
        self.login_attempts += 1

    def reset_login_attempts (self):
        self.login_attempts = 0
#Used Dicts to store user info.
users = {
        'user1' : {'first': 'kelsey', 'last': 'jones', 'email': 'user1@python.kom', 'username': 'user1', 'loca': 'CA'},
        'user2' : {'first': 'kyrie', 'last': 'irving', 'email': 'user2@python.kom', 'username': 'user2', 'loca': 'NJ'},
        'user3' : {'first': 'luka', 'last': 'doncic', 'email': 'user3@python.kom', 'username':  'user3', 'loca': 'NY'},
        'user4' : {'first': 'dereck', 'last': 'lively', 'email': 'user4@python.kom', 'username': 'user4', 'loca': 'MIA'},
        'user5' : {'first': 'dwight', 'last': 'powell', 'email': 'user5@python.kom', 'username': 'user5', 'loca': 'TX'},
        'user6' : {'first': 'maxi', 'last': 'kleber', 'email': 'user6@python.kom', 'username': 'USER5', 'loca': 'AL'},
        }


#Create Instances and Output
for userinfo in users.values():
    profile = User(userinfo['first'], userinfo['last'], userinfo['email'], userinfo['username'], userinfo['loca'])

print(f"number of logins: {profile.login_attempts}.")
profile.increment_login_attempts()
profile.increment_login_attempts()
profile.increment_login_attempts()
profile.increment_login_attempts()
profile.increment_login_attempts()
profile.increment_login_attempts()

#Display Increment Counter
print(f"number of logins: {profile.login_attempts}.")

#Reset Login Counter
profile.reset_login_attempts()
print(f"number of logins: {profile.login_attempts}.")
