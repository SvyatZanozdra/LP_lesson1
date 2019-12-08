eaters = input('Сколько человек делят пирог?: ')

def cut_cake(people):
    try:
        z = 1 / people
        print(f'Каждый получит {z} частей пирога')
    except (ZeroDivisionError, TypeError, ValueError):
        print('Не могу поделить')

print(cut_cake((eaters))