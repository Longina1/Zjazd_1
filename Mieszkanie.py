square_meters = int(input('What is the size of ypur apartment? '))
material = input('If your block is made of brick, enter: brick. If your block is prefabricated, enter: prefabricated ')

if material == 'brick':
    print('The cost of heating is', square_meters * 0.30, 'per day.')
if material == 'prefabricated':
    print('The cost of heating is', square_meters * 0.50, 'per day.')
