blocked_usernames = ['kamil', 'marek', 'mandarynka98', 'nowy1', 'pixi']

for username in blocked_usernames:
    username = input('Username: ')
    if (username in blocked_usernames):
        print('The username is already in use. Choose a different one.')
        break
    else:
        print('The username is available.')
        break





