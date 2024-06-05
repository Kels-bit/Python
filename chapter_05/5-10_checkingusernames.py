current_users = ['admin', 'Clown', 'foxes', 'hacker', 'snake', 'copy', 'guest']

new_users = ['book', 'chicken', 'clown', 'foxxes', 'snake', 'COPY']

new_current_users = []
for user in current_users:
    new_current_users.append(user.lower())

for nuser in new_users:
    if nuser.lower() in new_current_users:
        print(f"{nuser}, is taken choose another username.")
    else:
        print(f"{nuser} is available.")
