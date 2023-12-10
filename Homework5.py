def game(_question, _answer, _counterAnswers):

    correctAnswer = True

    while True:

        print(_question)
        userAnswer = input().lower()

        if userAnswer == _answer.lower():
            print('Ответ {} верен {}'.format(_answer, '!'))
            _counterAnswers[list(_counterAnswers.keys())[0]] += 1
            if correctAnswer:
                _counterAnswers[list(_counterAnswers.keys())[1]] += 1
            break
        else:
            print('Неверный ответ.')
            _counterAnswers[list(_counterAnswers.keys())[0]] += 1
            correctAnswer=False

    return _counterAnswers


if __name__ == '__main__':

    print('Hello')

    questionsAndAnswers = {'Какая версия языка сейчас актуальна?':'Python3',
                            'Какая кодировка используется в строках?': 'UTF8',
                            'Сколько значений есть у bool?': '2',
                            'VLIW-это архитектура каких процессоров?': 'Эльбрус',
                            'Что подходит для создания бесконечных циклов?': 'While',
                            'Можно ли изменить список после создания?': 'Да',
                            'Можно ли тип int перевести в str?': 'Да',
                            'Python относится к компилируемым языкам?': "Нет",
                            'Что используют для ускорения работы Python?': 'Модули',
                            'Да?': 'Да'}


    counterAnswers = {'Общее количество попыток = ': 0,
                     'Количество верных ответов = ': 0}

    for key, value in questionsAndAnswers.items():
        counterAnswers = game(_answer=value, _question=key, _counterAnswers=counterAnswers)

    print('Вы ответили на {} вопросов.'.format(len(questionsAndAnswers)))
    print(list(counterAnswers.keys())[0], list(counterAnswers.values())[0])
    print(list(counterAnswers.keys())[1], list(counterAnswers.values())[1])


question = ['Какая версия языка сейчас актуальна?', 2, 3 ,5]
answer = []
all_try = 0
correct_try = 0

for index in range(len(question)):
    correctAnswer = True
    while True:
        print(question[index])
        userAnswer = input().lower()
        if userAnswer == answer[index].lower():
            print('Ответ {} верен {}'.format(userAnswer, '!'))
            all_try += 1
            if correctAnswer:
                correct_try += 1
            break
        else:
            print('Неверный ответ.')
            all_try += 1
            correctAnswer=False

print('Вы ответили на {} вопросов.'.format(len(question)))
print(f'Общее количество попыток = {all_try}')
print(f'Количество верных ответов = {correct_try}')



