"""
Модуль работы с паролями пользователей

CHARS - константа, из которой будет формироваться новый пароль
"""

import random
import string

# CHARS = "~!@#$%^&*()_+=-0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
CHARS = string.ascii_letters + string.digits + string.punctuation


def get_new_password(length: int = 8) -> str:
    """
    Функция генерации паролей из N-символов

    :param length: Длина пароля
    :return: возвращается пароль в виде строки
    """

    pswd = ""

    for i in range(length):
        pswd += random.choice(CHARS)
    return pswd


def check_strong_password(pswd: str) -> bool:
    """
    Функция проверяет надежность пароля

    :param pswd: Пароль для проверки
    :return надежность пароля
    """

    if len(pswd) < 6:
        print("Недопустимый пароль")
        return False
    elif pswd.isdigit() or (pswd.isalpha() and pswd.islower()):
        print("Ненадежный пароль")
        return False
    elif (pswd.isdigit() and pswd.lower()) or (pswd.isalpha() and pswd.lower()):
        print("Слабый пароль")
        return True
    else:
        print("Надежный пароль")
        return True

