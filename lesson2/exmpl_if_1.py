balance = 1000
price = 200

print(bool(balance < 0 or price > balance))

if balance < 0 or price > balance:
    print('Пожалуйста, пополните баланс!')
else:
    print('Спасибо за покупку!')