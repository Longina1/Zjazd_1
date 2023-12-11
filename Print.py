#program, który wita uzytkownika.
#czesc albo dzien dobry, zaleznie od wieku
#Sznaowny Panie albo Szanowna Pani - w zależnosci od płci

first_name = input('Enter your name: ')
age = int(input('Enter your age: '))

if age > 18:
    if first_name[-1] == 'a':
        print('Witam Szanowną Panią!')
    else:
        print('Witam Szanownego Pana!')
elif age <= 18:
    print('Cześć ', first_name,'!')


first_name = input('Enter your name: ')
age = int(input('Enter your age: '))
gender = bool(int(input('Czy jesteś kobietą? Jeśli tak, napisz "1", jeśli nie - wpisz "0"')))

if age <= 18:
    print('Cześć, ', first_name, '.\nMasz', age, 'lat. Osiągniesz pełnoletniość za ', 18 - age, 'lat.')
else:
    if gender:
        print('Szanowna Pani', first_name, '.\nMa Pani ', age, 'lat.')
    else:
        print('Szanowny Panie ', first_name, '.\nMa Pan ', age, 'lat.')
