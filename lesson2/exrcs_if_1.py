user_age = input('Введите ваш возраст: ')
user_age_int = int(user_age)

def user_status (age):
    if age > 0 and age <= 6:
        return 'Медленно отойди (если умеешь) от клавиатуры...'
    if age > 6 and age <= 16:
        return 'Школолололо'
    if age > 16 and age <= 21:
        return 'Две пересдачи и ты в армии, сынок'
    else:
        return 'Еще немного потерпеть и пенсия'

a = user_status(user_age_int)
print(a)