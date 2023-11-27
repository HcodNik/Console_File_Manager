import platform
import sys
import os
import shutil
from file_manager.menu_mod import main_menu_input

menu_num = ''  # Глобальная


def ch_dir():  # смена рабочей директории
    print(f'Текущая директория: {os.getcwd()}')
    new_current_dir = input(r'Укажите новую директорию: ')

    try:
        print(f'Рабочая директорию изменена на {new_current_dir}')
        return os.chdir(new_current_dir)
    except:
        return print(f'Произошла ошибка {sys.exc_info()}')


def add_folder():  # создать каталог в тек. директории
    name_fold = input('Введите имя каталога: ')
    all_folder = view_folder_only()
    while name_fold in all_folder:
        print('Папка с таким именем уже существует!')
        break
    else:
        print(f'Папка "{name_fold}" успешно создана!')
        return os.mkdir(name_fold)


def view_file_only():  # посмотреть ТОЛЬКО файлы текущей директории
    cwd = os.listdir(os.getcwd())  # вывести список всех файлов и каталогов тек. директории
    dir_file = []
    for item in cwd:
        if os.path.isfile(item) == True:
            dir_file.append(item)
    return dir_file
    # return print(f'Список файлов текущей директории:{os.getcwd()}\n{'\n'.join(dir_file)}')


def view_folder_only():  # посмотреть ТОЛЬКО папки текущей директории
    cwd = os.listdir(os.getcwd())  # вывести список всех файлов и каталогов тек. директории
    dir_fold = []
    for item in cwd:
        if os.path.isdir(item) == True:
            dir_fold.append(item)
    return dir_fold
    # return print(f'Список папок текущей директории:{os.getcwd()}\n{'\n'.join(dir_fold)}')


def list_dir():  # просмотр содержимого рабочей директории
    return os.listdir(os.getcwd())


def del_file_only(name_f):  # удалить только файл
    if name_f in view_file_only():
        print(f'Файл "{name_f}" успешно удалён.')
        return os.remove(name_f)


def del_folder_only(name_f):  # удалить только папку
    if name_f in view_folder_only():
        print(f'Папка "{name_f}" успешно удалена.')
        return shutil.rmtree(name_f)


def del_file_folder():  # удалить файл/папку
    name_f = input('Введите имя файла/каталога для удаления: ')
    str = os.path.join(os.getcwd(), name_f)  # current_dir + '\\' + name_f ... <-- неправильная запись
    if os.path.isfile(str):
        return del_file_only(name_f)
    elif os.path.isdir(str):
        return del_folder_only(name_f)
    else:
        return print(f'Файла/папки с именем "{name_f}" не найдено!')


def copy_():  # КОПИРОВАТЬ ФАЙЛ/ПАПКУ
    copy_source = input('Укажите имя файла/папки текущей директории для создания копии: ')
    str = os.path.join(os.getcwd(), copy_source)  # current_dir + '\\' + name_f ... <-- неправильная запись
    if os.path.isfile(str):
        copy_dest = input('Укажите новое имя файла: ')
        print(f'Успешная копия в "{copy_dest}"')
        return shutil.copy2(str, os.path.join(os.getcwd(), copy_dest))
    elif os.path.isdir(str):
        copy_dest = input('Укажите новое имя папки: ')
        print(f'Успешная копия в "{copy_dest}"')
        return shutil.copytree(str, copy_dest)
    else:
        return print(f'Файла/папки с именем "{copy_source}" не найдено!')


if __name__ == '__main__':
    print(__name__)

    # print(os.getcwd())  # метод сообщает нам местоположение текущего рабочего каталога (CWD - Current working directory)
    # print(os.listdir(os.getcwd()))  # список всех файлов и каталогов в указанном каталоге, по умолчанию это текущий каталог
    # print(os.path.isfile(os.getcwd())) # проверяет, файл ли это
    # print(os.path.isdir(os.getcwd())) # проверяет, папка ли это
    # print(os.path.exists(os.getcwd())) # проверяет, существует ли указанный путь
    # print(f'Содержимое директории: {current_dir}\n', ',\n'.join(list_dir()))
    # print(os.path.basename(current_dir)) # конечная рабочая папка
