def discounted(price, discount, max_discount=20):
    price = abs(float(price))
    discount = abs(float(discount))
    if max_discount > 99:
        raise  ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

price_income = float(input('Введите цену: '))
discount_income = float(input('Введите скидку: '))

a = discounted(price_income, discount_income)

print(a)