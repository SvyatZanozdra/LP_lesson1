questions = {'Как дела?': 'Хорошо!', 'Что делаешь?': "Программирую"}
ask_user = input('')
done = False

while done == False:
    for question in questions.keys():
        if question == ask_user:
            print(questions[question])
        if question != ask_user:
            ask_user = input('')
            print('Спроси другое')
    continue