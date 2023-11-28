from file_manager.os_mod import *
from file_manager.author_mod import author
from file_manager.sysinfo_mod import sys_info
import bank_account.score


def sim_multi(sim, value):  # функция символы
    sim_multi = sim * value
    return print(sim_multi)


def main_menu_print():
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
    print('12. Главное меню')
    print('13. Выход')
    sim_multi('#', 50)


def main_menu_input():
    global menu_num
    menu_num = input(f'\n{os.getcwd()}> ')
    if menu_num == '1':
        add_folder()
    elif menu_num == '2':
        del_()
    elif menu_num == '3':
        copy_()
    elif menu_num == '4':
        print(',\n'.join(list_dir()))
    elif menu_num == '5':
        print(',\n'.join(view_folder_only()))
    elif menu_num == '6':
        print(',\n'.join(view_file_only()))
    elif menu_num == '7':
        sys_info()
    elif menu_num == '8':
        author()
    elif menu_num == '9':
        pass
    elif menu_num == '10':
        bank_account.score.score_func()
    elif menu_num == '11':
        ch_dir()
    elif menu_num == '12':
        main_menu_print()
    elif menu_num == '13':
        exit()
    else:
        print('Пункт меню указан неверно!')
        main_menu_print()
    main_menu_input()



if __name__ == '__main__':
    pass
