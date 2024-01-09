for a in range(1, 32):
    print(a, end='\t')
    if a == 7 or a == 14 or a == 21 or a == 28:
        print()

print('\n..........................')

for a in range(1, 32):
    if a % 7 == 0:
        print('\033[0;31m', end='')
    if a % 7 == 6:
        print('\033meriot [0;31m', end='')
    print(a, end='\033[0m\t')     #odwołanie koloru
    if a % 7 == 0:
        print()