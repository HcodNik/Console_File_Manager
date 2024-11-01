from function import *
from score import score_func

if __name__ == '__main__':
    main_menu = f"""
    +++++++++++ Файловый менеджер вер. 1.0 +++++++++++
    {sim_multi('=', 50)} 
    1:  Создать папку.
    2:  Удалить (файл/папку).
    3:  Копировать (файл/папку).
    4:  Просмотр содержимого рабочей директории.
    5:  Посмотреть только папки.
    6:  Посмотреть только файлы.
    7:  Просмотр информации об операционной системе.
    8:  Создатель программы.
    9:  Играть в игру "ВИКТОРИНА".
    10: Мой банковский счет.
    11: Смена рабочей директории.
    12: Вернуться в главное меню.
    0:  Выход из программы. 
    {sim_multi('=', 50)}"""

    print(main_menu)


def main_menu_input():
    input_menu_item = input(f'\nPS {os.getcwd()}> ')
    if input_menu_item.isdigit() == False or eval(input_menu_item) not in range(0, 13):
        print('Некорректный ввод! Введите цифру от 0 до 12...')
        return main_menu_input()
    else:
        input_menu_item = eval(input_menu_item)

    match input_menu_item:
        case 1:
            add_folder()
        case 2:
            del_()
        case 3:
            copy_()
        case 4:
            print(',\n'.join(list_dir()))
        case 5:
            print(',\n'.join(view_folder_only()))
        case 6:
            print(',\n'.join(view_file_only()))
        case 7:
            print(sys_info())
        case 8:
            author()
        case 9:
            custom_execfile('victory.py')
        case 10:
            score_func()
        case 11:
            ch_dir()
        case 12:
            print(main_menu)
        case 0:
            exit()
    return main_menu_input()


main_menu_input()
