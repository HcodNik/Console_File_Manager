import os
from manager_module.menu_module import main_menu_explorer
from manager_module.os_module import current_dir, view_file_only, view_folder_only


def del_file_only(name_f):  # удалить только файл
    if name_f in view_file_only():
        print(f'Файл "{name_f}" успешно удалён.')
        return os.remove(name_f)


def del_folder_only(name_f):  # удалить только папку
    if name_f in view_folder_only():
        print(f'Папка "{name_f}" успешно удалена.')
        return os.rmdir(name_f)


def del_file_folder():  # удалить файл/папку
    name_f = input('Введите имя файла/каталога для удаления: ')
    str = current_dir + '\\' + name_f
    if os.path.isfile(str):
        del_file_only(name_f)
    elif os.path.isdir(str):
        del_folder_only(name_f)
    else:
        print(f'Файла/папки с именем "{name_f}" не найдено!')
    main_menu_explorer()
