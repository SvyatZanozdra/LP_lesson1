user_name = input('Введите ваше имя: ')
user_last_name = input('Введите вашу фамилию: ')

user_info = {
    'first_name': {user_name},
    'last_name': {user_last_name}
}

print(user_info['first_name'])