import platform
import os
from file_manager.menu_mod import *


current_dir = os.getcwd() # ГЛОБАЛЬНАЯ...текущий каталог

def add_folder(): # создать каталог в тек. директории
    name_fold = input('Введите имя каталога: ')
    while os.path.exists(name_fold) == True:
        print('Каталог с таким именем уже существует!')
        break
    else:
        print(f'Папка "{name_fold}" успешно создана.')
        return os.mkdir(name_fold)
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


if __name__ == '__main__':
    print(os.getcwd())  # метод сообщает нам местоположение текущего рабочего каталога (CWD - Current working directory)
    print(os.listdir(os.getcwd()))  # список всех файлов и каталогов в указанном каталоге, по умолчанию это текущий каталог
    print(os.path.isfile(os.getcwd())) # проверяет, файл ли это
    print(os.path.isdir(os.getcwd())) # проверяет, папка ли это
    print(os.path.exists(os.getcwd())) # проверяет, существует ли указанный путь
    print(f'Содержимое директории: {current_dir}\n', ',\n'.join(list_dir()))

