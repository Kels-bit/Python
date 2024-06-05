usernames =[]
if usernames:
    for users in usernames:
        if users == 'admin':
            print("Hello admin, would you like a status report?")

        else:
            print(f"Hello {users}, thank you for logging in again.")
else:
    print("We need to find some users!")
