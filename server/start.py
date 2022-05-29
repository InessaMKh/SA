def start_server(host, port, user, password):
    """

    :param host:
    :param port:
    :param user:
    :param password:
    :return:
    """
    if not password:
        raise ConnectionError("Отсутствует пароль ")

    print(f'Сервер {host} запущен в порту {port}')

    if user == "test":
        print(f'Сервер в тестовом режиме, пользователь {user}')
    else:
        print(f'Сервер в штатном режиме, пользователь {user}')


if __name__ == "__main__":
    import config

    host = config.HOST
    port = config.PORT
    user, password = config.test_config().values()

    start_server(host=host, port=port, user=user, password=password)