a = 5

print(id(a))

print('Are you nice? yes/no ')
reply = input()

if reply == 'yes':
    user_is_nice = True
else:
    user_is_nice = False

if user_is_nice:
    print('Welcome')
else:
    print('You are not welcome')