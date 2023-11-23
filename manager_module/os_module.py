import platform, os
from manager_module.menu_module import main_menu_explorer




def view_file_only(): # посмотреть ТОЛЬКО файлы текущей директории
    cwd = os.listdir(os.getcwd()) # вывести список всех файлов и каталогов тек. директории
    dir_file = []
    for item in cwd:
        if os.path.isfile(item) == True:
            dir_file.append(item)
    return dir_file
    #return print(f'Список файлов текущей директории:{os.getcwd()}\n{'\n'.join(dir_file)}')

def view_folder_only(): # посмотреть ТОЛЬКО папки текущей директории
    cwd = os.listdir(os.getcwd()) # вывести список всех файлов и каталогов тек. директории
    dir_fold = []
    for item in cwd:
        if os.path.isdir(item) == True:
            dir_fold.append(item)
    return dir_fold
    #return print(f'Список папок текущей директории:{os.getcwd()}\n{'\n'.join(dir_fold)}')

def sys_info(): # информация о системе
    os_info = platform.uname()
    print(f"Операционная система: {os_info.system} {os_info.release}")
    print(f"Сборка ОС: {os_info.version}")
    print(f"Имя устройства: {os_info.node}")
    print(f"Архитектура: {','.join(platform.architecture())}")
    print(f"Процессор: {platform.processor()}")

def del_file(): # удалить файл/папку из тек. директории
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

def add_folder(): # создать каталог в тек. директории
    name_fold = input('Введите имя каталога: ')
    while os.path.exists(name_fold) == True:
        print('Каталог с таким именем уже существует!')
        break
    else:
        print(f'Папка "{name_fold}" успешно создана.')
        return os.mkdir(name_fold)
    main_menu_explorer()



    if __name__ == '__main__':
        print(os.getcwd())  # метод сообщает нам местоположение текущего рабочего каталога (CWD - Current working directory)
        print(os.listdir(os.getcwd()))  # список всех файлов и каталогов в указанном каталоге, по умолчанию это текущий каталог
        print(os.path.isfile(os.getcwd())) # проверяет, файл ли это
        print(os.path.isdir(os.getcwd())) # проверяет, папка ли это
        print(os.path.exists(os.getcwd())) # проверяет, существует ли указанный путь




