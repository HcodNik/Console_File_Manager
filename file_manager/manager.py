import os
import os_mod
from author_mod import author
from menu_mod import main_menu_explorer
from os_mod import *
from del_mod import *



# print(os.stat in os.supports_dir_fd)
# print(os.pardir)
# print(os.path.abspath(os.path.join(os.getcwd(), os.pardir))) # родительская директория

# cwd = os.path.join(os.getcwd() + r'\111')


# def sm_dir():
#      global current_dir
#      current_dir =  os.chdir(os.path.join(current_dir, '111'))


# print(os.chdir(r'C:/Users/Admin/PycharmProjects/Console_File_Manager/file_manager/111'))
#
# print(current_dir)


# print(os_mod.__name__)
#
# print(f'Старый путь: {os.getcwd()}')
#
# current_dir = r'C:\Users\Admin\PycharmProjects\Console_File_Manager\file_manager\111'
#
# try:
#     os.chdir(current_dir)
#     print("Current working directory: {0}".format(os.getcwd()))
# except FileNotFoundError:
#     print("Directory: {0} does not exist".format(current_dir))
# except NotADirectoryError:
#     print("{0} is not a directory".format(current_dir))
# except PermissionError:
#     print("You do not have permissions to change to {0}".format(current_dir))
#
print(f'Новый путь: {os.getcwd()}')
del_file_folder()