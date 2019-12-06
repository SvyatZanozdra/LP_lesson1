names = ['Вася', 'Маша', 'Саша', 'Петя', 'Валера', 'Даша']

name = None
x = 0

while name != 'Валера':
    name = names[x]
    x += 1
    if name == 'Валера':
        print(f'{name} нашелся')