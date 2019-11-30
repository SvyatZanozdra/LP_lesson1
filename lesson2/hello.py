import datetime

greeting = input('Привет, напиши свое имя: ')

user_name = greeting.capitalize()

def time_of_day(x):
    if x > 22 and x < 24:
        return 'Доброй ночи'
    elif x >= 0 and x < 4:
        return 'Доброй ночи'
    elif x >= 5 and x < 12:
            return 'Доброе утро'
    elif x >= 12 and x < 17:
            return 'Добрый день'
    else:
        return 'Добрый вечер'

from datetime import datetime
now = datetime.now()
a = now.hour

polite_greeting = time_of_day(a)

print(f'{polite_greeting}, {user_name}!')