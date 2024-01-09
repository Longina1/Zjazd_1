for a in range(10):
    print(a+1)

for a in range(1, 10):
    print(a+1)

for a in range(6, 10):
    print(a, a, a, a, a, a, sep=' ')

for a in range(1, 10):
    print(a, end='\t')
print('\n........................')

for a in range(1, 11):
    print(a, end='\t')
print() #tworzy Enter
print('\n........................')

for a in range(0, 11):
    for b in range(0, 11):
        if a == 0 and b == 0:
            print('\033[0;31m*\033[0m', sep='', end='\t')
        elif a == 0:
            print('\033[0;31m', b, '\033[0m', sep='', end='\t')
        elif b == 0:
            print('\033[0;31m', a, '\033[0m', sep='', end='\t')
        elif a == b:
            print('\033[0;31m', a, '\033[0m', sep='', end='\t')
        else:
            print(a * b, end='\t')
    print()
