list = ['Anna', 'Sylwia', 'Adam', 'Marek', 'Aleksandra']


for name in list:
    if name[0] == 'A':
        print(name)


if list[0][0] == 'A':
    print(list[0])

for name in list:
    if name.startswith('A'):
        print(name)
print(name)