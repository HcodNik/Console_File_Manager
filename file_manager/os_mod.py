import platform
import sys
import os
from file_manager.menu_mod import *


current_dir = os.getcwd() # ГЛОБАЛЬНАЯ...текущий каталог


def ch_dir(): # смена рабочей директории
    global current_dir
    print(f'Текущая директория: {current_dir}')
    current_dir = input(r'Укажите новую директорию: ')
    try:
        os.chdir(os.path.join(os.getcwd(), current_dir))
        print(f'Рабочая директория изменена на {current_dir}')
    except:
        print(f'Произошла ошибка {sys.exc_info()}')
        print('Восстанавливаем рабочую директорию на прежнюю')
    finally:
        # print('Восстанавливаем рабочую директорию на прежнюю')
        print(f'Текущая рабочая директория - {os.getcwd()}')
    main_menu_explorer()

def add_folder(): # создать каталог в тек. директории
    name_fold = input('Введите имя каталога: ')
    all_folder = view_folder_only()
    while name_fold in all_folder:
        print('Папка с таким именем уже существует!')
        break
    else:
        print(f'Папка "{name_fold}" успешно создана!')
        os.mkdir(name_fold)
    main_menu_explorer()


def view_file_only(): # посмотреть ТОЛЬКО файлы текущей директории
    global current_dir
    cwd = os.listdir(current_dir) # вывести список всех файлов и каталогов тек. директории
    dir_file = []
    for item in cwd:
        if os.path.isfile(item) == True:
            dir_file.append(item)
    return dir_file
    #return print(f'Список файлов текущей директории:{os.getcwd()}\n{'\n'.join(dir_file)}')

def view_folder_only(): # посмотреть ТОЛЬКО папки текущей директории
    global current_dir
    cwd = os.listdir(current_dir) # вывести список всех файлов и каталогов тек. директории
    dir_fold = []
    for item in cwd:
        if os.path.isdir(item) == True:
            dir_fold.append(item)
    return dir_fold
    #return print(f'Список папок текущей директории:{os.getcwd()}\n{'\n'.join(dir_fold)}')

def list_dir(): # просмотр содержимого рабочей директории
    return os.listdir(current_dir)


# КОПИРОВАТЬ ФАЙЛ/ПАПКУ
# def copy_file_folder:
#     copy_item = input('Укажите имя файла/папки текущей директории для создания копии: ')
#     while copy_item is not list_dir():
#         print('Файла/папки с таким именем не найдено!')
#         break
#     else:
#         if os.path.isfile(copy_item):






if __name__ == '__main__':
    print(__name__)


    # print(os.getcwd())  # метод сообщает нам местоположение текущего рабочего каталога (CWD - Current working directory)
    # print(os.listdir(os.getcwd()))  # список всех файлов и каталогов в указанном каталоге, по умолчанию это текущий каталог
    # print(os.path.isfile(os.getcwd())) # проверяет, файл ли это
    # print(os.path.isdir(os.getcwd())) # проверяет, папка ли это
    # print(os.path.exists(os.getcwd())) # проверяет, существует ли указанный путь
    # print(f'Содержимое директории: {current_dir}\n', ',\n'.join(list_dir()))
    # print(os.path.basename(current_dir)) # конечная рабочая папка
