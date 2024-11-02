import random
from function import *

def victory():
    print('Игра "ВИКТОРИНА"\n')

    person_birtday = {
        'Александр Пушкин': '06.06.1799',
        'Альберт Эйнштейн': '14.03.1879',
        'Никола Тесла': '10.07.1856',
        'Алан Тьюринг': '23.06.1912',
        'Стив Джобс': '24.02.1955',
        'Джефф Безос': '12.01.1964',
        'Билл Гейтс': '28.10.1955',
        'Уоррен Баффет': '30.08.1930',
        'Владимир Путин': '07.10.1952',
        'Джозеф Байден-младший': '20.11.1942',
        'Дональд Трамп': '14.06.1946'}

    person_birtday_random = random.sample(list(person_birtday.items()), 5)

    count = 0  # счётчик верных ответов

    for i in range(len(person_birtday_random)):
        user_response = input(person_birtday_random[i][0] + ' - укажите дату рождения (DD.MM.YYYY): ')
        data_string_in_data_word(user_response)
        if data_string_in_data_word(user_response) == 0:
            print(f'Неверно! Верный ответ - {data_string_in_data_word(person_birtday_random[i][1])}')
        else:
            count += 1
            print('Верно!')

    print(f'Правильных ответов: {calc_the_percentage(len(person_birtday_random), count)} %')
    print(f'Неправильных ответов: {100 - calc_the_percentage(len(person_birtday_random), count)} %')
