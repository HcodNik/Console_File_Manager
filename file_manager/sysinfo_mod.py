import platform


def sys_info():  # информация о системе
    os_info = platform.uname()
    print(f"Операционная система: {os_info.system} {os_info.release}")
    print(f"Сборка ОС: {os_info.version}")
    print(f"Имя устройства: {os_info.node}")
    print(f"Архитектура: {','.join(platform.architecture())}")
    print(f"Процессор: {platform.processor()}")


if __name__ == '__main__':
    pass
