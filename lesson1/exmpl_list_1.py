phones = ['iPhone Xs', 'Samsung Galaxy S10', 'Xiaomi Mi8']
total_list = len(phones)
count_iPhone_Xs = phones.count('iPhone Xs')
count_Samsung_Galaxy_S10 = phones.count('Samsung Galaxy S10')
count_Xiaomi_Mi8 = phones.count('SXiaomi Mi8')

print(f'Список всех телефонов: {phones}')
print(f'Всего телефонов: {total_list}')
phones.append('iPhone Xs')
print(f'Список всех телефонов: {phones}')
print(f'Всего телефонов: {total_list}')

print(f'Количество iPhone Xs: {count_iPhone_Xs}')
print(phones.count('iPhine 9'))