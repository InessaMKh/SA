"""
Модуль, в котором хранится конфигурация приложения
"""

HOST: str = "127.0.0.1"
PORT: str = "1234"


def test_config():
    return {"user": "test", "password": "012345"}


def real_config():
    return {"user": "admin", "password": "qwerty"}
