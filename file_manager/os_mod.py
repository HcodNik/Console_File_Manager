import platform
import sys
import os
import shutil
from file_manager.menu_mod import *

menu_num = ''  # ГЛОБАЛЬНАЯ...текущий каталог


def list_dir():  # просмотр содержимого рабочей директории списком
    return os.listdir(os.getcwd())


def ch_dir():  # смена рабочей директории
    print(f'Текущая директория: {os.getcwd()}')
    current_dir = input(r'Укажите новую директорию: ')
    try:
        current_dir = os.chdir(os.path.join(os.getcwd(), current_dir))
        print(f'Рабочая директория изменена на {os.getcwd()}')
    except:
        print(f'Произошла ошибка {sys.exc_info()}')


def add_folder():  # создать каталог в тек. директории
    name_fold = input('Введите имя каталога: ')
    while name_fold in view_folder_only():
        print('Папка с таким именем уже существует!')
        break
    else:
        print(f'Папка "{name_fold}" успешно создана!')
        return os.mkdir(name_fold)


def view_file_only():  # посмотреть ТОЛЬКО файлы текущей директории
    cwd = list_dir()  # вывести список всех файлов и каталогов тек. директории
    dir_file = []
    for _ in cwd:
        if os.path.isfile(_) == True:
            dir_file.append(_)
    return dir_file
    # return print(f'Список файлов текущей директории:{os.getcwd()}\n{'\n'.join(dir_file)}')


def view_folder_only():  # посмотреть ТОЛЬКО папки текущей директории
    cwd = list_dir()
    dir_fold = []
    for _ in cwd:
        if os.path.isdir(_) == True:
            dir_fold.append(_)
    return dir_fold
    # return print(f'Список папок текущей директории:{os.getcwd()}\n{'\n'.join(dir_fold)}')


# def copy_file_folder():  # КОПИРОВАТЬ ФАЙЛ/ПАПКУ
#     copy_item = input('Укажите имя файла/папки текущей директории для создания копии: ')
#     while copy_item is not list_dir():
#         print('Файла/папки с таким именем не найдено!')
#         break
#     else:
#         if os.path.isfile(copy_item):


if __name__ == '__main__':
    pass

    # print(os.getcwd())  # метод сообщает нам местоположение текущего рабочего каталога (CWD - Current working directory)
    # print(os.listdir(os.getcwd()))  # список всех файлов и каталогов в указанном каталоге, по умолчанию это текущий каталог
    # print(os.path.isfile(os.getcwd())) # проверяет, файл ли это
    # print(os.path.isdir(os.getcwd())) # проверяет, папка ли это
    # print(os.path.exists(os.getcwd())) # проверяет, существует ли указанный путь
    # print(f'Содержимое директории: {current_dir}\n', ',\n'.join(list_dir()))
    # print(os.path.basename(current_dir)) # конечная рабочая папка
