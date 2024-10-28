import platform


def sys_info():  # информация о системе
    os_info = platform.uname()
    return f"""
    Операционная система: {os_info.system} {os_info.release}
    Сборка ОС: {os_info.version}")
    Имя устройства: {os_info.node}")
    Архитектура: {','.join(platform.architecture())}")
    Процессор: {platform.processor()}"""

if __name__ == '__main__':
    print(sys_info())