print('Witamy w programie!')
x =int(input('Ile razy chcesz wykonać pętlę?'))


for i in range(x):
    print('To jest ', x, ' wykonanie.')
    print('Lecimy dalej')
print('Koniec pętli')

list = [1, 5, 3, 24, 15, 6, 8, 12, 31]
print('1.', list[0], ',', '2.', list[1], ',', '3.', list[2], ',', '4.', list[3], ',', '5.', list[4], ',', '6.', list[5], ',', '7.', list[6], ',', '8.', list[7], ',', '9.', list[8])

for x in list:
    if x % 2 == 0:
        print(x)

for x in list:
    if x > 10:
        print(x)




