import manager_module.menu_module
from  manager_module.menu_module import *
import os
import manager_module.os_module
from  manager_module.os_module import *



def view_only_files():
    cont_dir = os.listdir()
    dir_files_only = []
    for file in cont_dir:
        if os.path.isfile(os.path.join(file)):
            dir_files_only.append(file)
    print(',\n'.join(dir_files_only))


def view_only_folders():
    cont_dir = os.listdir()
    dir_files_only = []
    for file in cont_dir:
        if os.path.isfile(os.path.join(file)):
            dir_files_only.append(file)
    print(dir_files_only)




