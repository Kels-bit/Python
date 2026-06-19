""" Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user. """


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
    profile.describe_user()
    profile.greet_user()

