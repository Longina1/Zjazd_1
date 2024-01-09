given_number = int(input('Enter a number:  '))

if given_number == 0:
    print(f'Your number is {given_number}.')
elif given_number > 0:
    print(f'The negative of your number is -{given_number}.')
else:
    print(f'Your number is negative ({given_number}).')

given_number = int(input('Enter a number:  '))
if given_number > 0:
    output = -given_number
else:
    output = given_number
print(output)


given_number = int(input('Enter a number:  '))
if given_number > 0:
    given_number = -given_number
print(given_number)


given_number = int(input('Enter a number:  '))
output = -abs(given_number)
print(output)