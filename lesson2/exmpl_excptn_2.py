inpt_price = input('')
inpt_discount = input('')

def discounted(price, discount):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        if discount >= 100:
            price_with_discount = price
        else:
            price_with_discount = price - (price * discount / 100)
        return price_with_discount
    except ValueError:
        return 'Ты ввел буквы, долбоеб! Введи циферки'

print(discounted(inpt_price, inpt_discount))