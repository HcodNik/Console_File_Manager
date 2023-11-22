import platform, os
from manager_module.menu_module import main_menu_explorer


def sys_info(): # информация о системе
    os_info = platform.uname()
    print(f"Операционная система: {os_info.system} {os_info.release}")
    print(f"Сборка ОС: {os_info.version}")
    print(f"Имя устройства: {os_info.node}")
    print(f"Архитектура: {','.join(platform.architecture())}")
    print(f"Процессор: {platform.processor()}")

def del_file(): # удалить файл/папку
    name_file = input('Введите имя файла для удаления: ')
    while os.path.exists(name_file) != True:
        print('Файл/папка с таким именем не найдены!')
        break
    if os.path.isdir(name_file):
        print(f'Папка /{name_file}/ успешно удалена.')
        return os.rmdir(name_file)
    elif os.path.isfile(name_file):
        print(f'Файл /{name_file}/ успешно удалён.')
        return os.remove(name_file)
    main_menu_explorer()

def add_folder(): # создать каталог
    name_fold = input('Введите имя каталога: ')
    while os.path.exists(name_fold) == True:
        print('Каталог с таким именем уже существует!')
        break
    else:
        print(f'Папка "{name_fold}" успешно создана.')
        return os.mkdir(name_fold)
    main_menu_explorer()

    if __name__ == '__main__':
        pass