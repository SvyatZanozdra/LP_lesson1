def weather(temperature):
    if temperature <= 0:
        return 'На улице холодно'
    elif 1 <= temperature <= 15:
        return 'На улице прохладно'
    elif 16 <= temperature <= 25:
        return 'На улице тепло'
    else:
        return 'На улице жарко'

print(weather(-2))
print(weather(30))
print(weather(12))