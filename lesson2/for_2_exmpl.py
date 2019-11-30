school_stat = [
    {'school_class': '4a', 'score': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'score': [4, 3, 5, 4, 4]},
    {'school_class': '5a', 'score': [4, 5, 3, 4, 4]},
    {'school_class': '5b', 'score': [3, 4, 3, 4, 4]},
    {'school_class': '6a', 'score': [3, 2, 3, 2, 3]},
    {'school_class': '6b', 'score': [3, 5, 3, 4, 3]},
    {'school_class': '7a', 'score': [4, 5, 5, 5, 4]},
    ]

result1 = len(school_stat[1]['score'])
result2 = sum(school_stat[1]['score'])
print(result1, result2)

avg_score_class = sum(school_stat[0]['score']) / len(school_stat[0]['score'])
print(avg_score_class)

for score in school_stat:
    