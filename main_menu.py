import os
import shutil

# ************ФУНКЦИИ************
def sim_multi(sim, value): # функция символы
    sim_multi = sim * value
    return print(sim_multi)

def add_folder(): # создать каталог
    name_fold = input('Введите имя каталога: ')
    while os.path.isdir(name_fold) == True:
        print('Каталог с таким именем уже существует!')
        return add_folder()
    else:
        print(f'Папка "{name_fold}" успешно создана.')
        main_menu_explorer()
        return os.mkdir(name_fold)

# def del_file(): # удалить файл
#     name_file = input('Введите имя файла для удаления: ')
#     while os.path.isfile(name_file) != True:
#         os.remove(name_file)
#     else:
#         print('Файл не найден!')
#         return del_file()


def main_menu_explorer():
    print("\033[3m\033[33m\033[41m{}\033[0m".format("Файловый менеджер вер. 1.0"))
    sim_multi('#', 50)
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Посмотреть только папки')
    print('6. Посмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Выход')
    sim_multi('#', 50)

print(os.path.isfile('222.py'))
print(os.path.isdir('222'))