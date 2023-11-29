import sys
import os
import shutil

menu_num = ''  # ГЛОБАЛЬНАЯ...текущий каталог


def list_dir():  # просмотр содержимого рабочей директории списком
    return os.listdir(os.getcwd())


def ch_dir():  # смена рабочей директории
    print(f'Текущая директория: {os.getcwd()}')
    current_dir = input(r'Укажите новую директорию: ')
    try:
        os.chdir(os.path.join(os.getcwd(), current_dir))
        print(f'Рабочая директория изменена на {os.getcwd()}')
    except:
        print(f'Произошла ошибка {sys.exc_info()}')


def add_folder():  # создать каталог в тек. директории
    name_fold = input('Введите имя каталога: ')
    try:
        if name_fold in view_folder_only():
            print('Папка с таким именем уже существует!')
        elif name_fold == '':
            print('Вы не указали имя папки!')
            add_folder()
        elif os.error(22):
            print('Синтаксическая ошибка в имени папки!')
            add_folder()
        else:
            print(f'Папка "{name_fold}" успешно создана!')
            return os.mkdir(name_fold)
    except:
        return print(f'Произошла ошибка {sys.exc_info()}')


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


def del_():
    del_name = input('Введите имя файла/папки текущей директории для удаления: ')
    if del_name in view_file_only():
        print(f'Файл "{del_name}" успешно удалён')
        return os.remove(os.path.join(os.getcwd(), del_name))
    elif del_name in view_folder_only():
        print(f'Каталог "{del_name}" успешно удалён')
        return shutil.rmtree(os.path.join(os.getcwd(), del_name))
    else:
        print(f'Файл/каталог с именем "{del_name}" не найден')


def copy_():  # КОПИРОВАТЬ ФАЙЛ/ПАПКУ
    name = input('Укажите имя файла/папки текущей директории для создания копии: ')
    if name in list_dir():
        if os.path.isfile(os.path.join(os.getcwd(), name)):
            new_name = input('Укажите новое имя файла: ')
            while new_name in view_file_only():
                print(f'Файл с именем "{new_name}" уже существует!')
                return copy_()
                break
            print(f'Копия "{new_name}" создана."')
            return shutil.copy2(name, new_name)
        if os.path.isdir(os.path.join(os.getcwd(), name)):
            new_name = input('Укажите новое имя папки: ')
            while new_name in view_folder_only():
                print(f'Папка с именем "{new_name}" уже существует!')
                return copy_()
                break
            print(f'Копия "{new_name}" создана.')
            return shutil.copytree(name, new_name)
    else:
        return print('Файл/папка с таким именем не найдена!')


if __name__ == '__main__':
    pass

    # print(os.getcwd())  # метод сообщает нам местоположение текущего рабочего каталога (CWD - Current working directory)
    # print(os.listdir(os.getcwd()))  # список всех файлов и каталогов в указанном каталоге, по умолчанию это текущий каталог
    # print(os.path.isfile(os.getcwd())) # проверяет, файл ли это
    # print(os.path.isdir(os.getcwd())) # проверяет, папка ли это
    # print(os.path.exists(os.getcwd())) # проверяет, существует ли указанный путь
    # print(f'Содержимое директории: {current_dir}\n', ',\n'.join(list_dir()))
    # print(os.path.basename(current_dir)) # конечная рабочая папка
