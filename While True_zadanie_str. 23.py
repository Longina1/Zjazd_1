secret_number = 15
guess = int(input('Enter a number: '))

while guess > secret_number:
    if guess == secret_number:
        print('Your number is equal to the number selected by the system.')
        break
    elif guess > secret_number:
        print('Your number is greater than the number selected by the system.')
        break
    else:
        print('Your number is less than the number selected by the system.')
        break


