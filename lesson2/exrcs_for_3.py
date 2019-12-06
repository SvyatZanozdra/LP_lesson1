school_stat = [
    {'school_class': '4a', 'score': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'score': [4, 3, 5, 4, 4]},
    {'school_class': '5a', 'score': [4, 5, 3, 4, 4]},
    {'school_class': '5b', 'score': [3, 4, 3, 4, 4]},
    {'school_class': '6a', 'score': [3, 2, 3, 2, 3]},
    {'school_class': '6b', 'score': [3, 5, 3, 4, 3]},
    {'school_class': '7a', 'score': [4, 5, 5, 5, 4]},
    ]

class_score = 0
class_number = 0
avg_score_list = []
class_number_list = []
total_list = []

for class_score in range(len(school_stat)):
    avg_score_list.append(sum(school_stat[class_score]['score']) / len(school_stat[class_score]['score']))

for class_number in school_stat:
    class_number_list.append(class_number['school_class'])

print(f'Средняя оценка по школе: {sum(avg_score_list) / len(avg_score_list)}')

for avg_class_score in range(len(class_number_list)):
    print(f'Средняя оценка по {class_number_list[avg_class_score]}: {avg_score_list[avg_class_score]}')