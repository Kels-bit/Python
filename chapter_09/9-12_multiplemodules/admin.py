from user import User

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
