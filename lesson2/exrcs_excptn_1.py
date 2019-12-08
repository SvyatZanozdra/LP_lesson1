questions = {'Как дела?': 'Хорошо!', 'Что делаешь?': "Программирую"}
ask_user = input('')

while True:
    try:
        for question in questions.keys():
            if question == ask_user:
                print(questions[question])
            else:
                ask_user = input('')
                print('Спроси другое')
    except KeyboardInterrupt:
        print('Пока!')
        break
        continue