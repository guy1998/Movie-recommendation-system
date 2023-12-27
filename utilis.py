
def authenticate(username, password, action, counter_action):
    with open('users.txt', 'r') as file:
        for line in file:
            user = line.split()
            if username == user[1] and password == user[2]:
                action()
                return

    counter_action()