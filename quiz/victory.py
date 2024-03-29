import random
import file_manager.menu_mod


def victory():
    birtday = {
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
    }

    day_list = ['первое', 'второе', 'третье', 'четвёртое',
                'пятое', 'шестое', 'седьмое', 'восьмое',
                'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
                'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
                'двадцать первое', 'двадцать второе', 'двадцать третье',
                'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
                'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
                'тридцатое', 'тридцать первое']

    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    catch0 = 0  # счётчик правильных ответов
    catch1 = 0  # счётчик неправильных ответов

    quest_items = random.sample(list(birtday.items()), 5)

    for i in range(len(quest_items)):
        quest_user = input(f'{''.join(quest_items[i][0])} - укажите дату рождения в формате dd.mm.yyyy: ')
        if quest_items[i][1] == quest_user:
            catch0 += 1
            print('Верно!')
        else:
            catch1 += 1
            cor_answ = quest_items[i][1].split('.')  # превращаем правильный ответ в список
            cor_answ = (f'Неверно! '
                        f'Правильный ответ: {day_list[int(cor_answ[0]) - 1]} {month_list[int(cor_answ[1]) - 1]} {cor_answ[2]} года')
            print(cor_answ)

    print(f'Правильных ответов: {catch0} ({int(catch0 * 100 / 5)}%)')
    print(f'Неправильных ответов: {catch1} ({int(catch1 * 100 / 5)}%)')
    return file_manager.menu_mod.main_menu_input()


