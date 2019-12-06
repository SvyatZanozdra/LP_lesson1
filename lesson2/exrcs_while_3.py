questions = {'Как дела?': 'Хорошо!', 'Что делаешь?': "Программирую"}

while True:
    ask_user = input('')
    for question in questions.keys():
        if question == ask_user:
            print(questions[question])
            break
        else:
            print(f'А сам как думаешь?')