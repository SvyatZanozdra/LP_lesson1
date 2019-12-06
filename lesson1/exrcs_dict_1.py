dictionarie = {
    "city": 'Москва', 
    "temperature": 20
    }

print(dictionarie['city'],dictionarie['temperature'])

a = input('Насколько должно стать теплее: ')
b = int(a)
dictionarie["temperature"] = dictionarie['temperature'] + b

print(dictionarie['temperature'])