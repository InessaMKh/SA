"""
Модуль для работы с базой данных
"""
import time

users = {}


def add_user(login: str, password: str) -> bool:
    """
    Функция добавляет пользователя в базу данных с проверкой уникальности пользователя

    :param login: Логин
    :param password: Пароль
    :return: True, если добавлен успешно, иначе False
    """
    if login not in users:
        users[login] = password
        print(f"{time.ctime()} - Пользователь {login} добавлен")
        return True
    else:
        print(f'{time.ctime()} - Пользователь {login} уже существует')
        return False

