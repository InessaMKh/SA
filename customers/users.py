"""
Модуль регистрации и/или генерации новых пользователей
"""

import random
import string
from server.models import add_user
from customers.password import get_new_password, check_strong_password


def get_new_user_name_random(name_length: int = 0) -> str:
    """
    Функция генерирует новое имя пользователя

    :param name_length: Длина нового имени
    :return: Новое имя пользователя
    """

    random_name = ""
    if name_length == 0:
        name_length = random.randint(5, 12)

    for i in range(name_length):
        random_name += random.choice(string.ascii_letters)

    return random_name

    # for i in range(15):
    #     login = get_new_user_name_random()
    #     pswd = get_new_password()
    #
    #     if check_strong_password(pswd):
    #         add_user(login, pswd)


class User:

    def get_new_user_name(self, login, pswd):
        print("Добавление пользователя в систему")
        login = input("Login: ") # для самостоятельного ввода нового пользователя
        pswd = input("Password: ")
        if check_strong_password(pswd):
           add_user(login, pswd)


    add_user("Inessa", get_new_password())
    add_user("Alena", get_new_password())
    add_user("Alena", get_new_password())





