regular_price = 3
special_offer = 3 * 0.80 * 3

cart = int(input('How many tomatoes do you want to buy? '))
cart_value = round(cart // 3 * special_offer + cart % 3 * 3, 2)
print(f'You need to pay {cart_value}.')
