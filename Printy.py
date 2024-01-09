a = 'Hello'
b = 'world!'

print(a, b)
print(a + ' ' + b)
print(a, b, sep=' ')

for i in range (3):
    print(a, b, sep=' | ')

print(a, end='')
print(b)

a = '\033[0;31mHello'
print(a)