i = 1
while i < 6:
    print(i)
    i = i + 1

standard_password = '123'
user_password = input('Enter password: ')
while user_password != standard_password:
    user_password = input('Invalid password. Enter password: ')

print('Correct password. Access granted.')

min_age = 18
user_age = int(input('Enter your age: '))
while user_age < min_age:
    user_age = int(input('Enter your age: '))
    print('Under the applicable regulations, age needs to be verified.')
print('Age verified. Welcome!')
