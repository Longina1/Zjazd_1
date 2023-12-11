standard_age = 18
user_age = int(input('Enter your age: '))

while True:
    if user_age >= standard_age:
        print('You are of age.')
        break
    elif user_age >= 13:
        print('Submit your parent or guardian consent.')
        break
    elif user_age >= 8:
        print('Submit an opinion issued by a psycologist.')
    else:
        print('Unfortunately, you are too young.')
        user_age = int(input('Enter your age: '))
print('To be continued')

while True:
    price = float(input('Enter the price ranging 1 to 1000: '))
    if 1 <= price <= 1000:
        break
    else:
        print('Invalid price. Enter the price.')
print('Price accepted')
