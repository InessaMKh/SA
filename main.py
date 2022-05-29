from customers.basket import Basket
from customers.password import check_strong_password
from hardware_store.category import categories

users = {}


def login(username: str):
    """
    Модуль регистрации пользователя
    :param login: пользовательский логин
    :param pswd: пользовательский пароль
    :return: Пользователь добавлен
    """
    password = input('Ваш пароль: ')

    return password == users[username]["password"]


def signUp(username):
    password = input('Ваш пароль: ')
    while True:
        password = input('Ваш пароль: ')
        if not check_strong_password(password):
            continue
        passConfirm = input('Подтверждение пароля: ')

        if passConfirm == password:
            users[username] = {
                'password': password,
                'basket': Basket()
            }
            return True
        else:
            print("Пароли не совпадают")


def showCategories():
    print('Выберите категорию:')
    for category in categories:
        print(str(categories.index(category)) + ': ' + category.title)


def showProducts(category):
    print('Выберите товар:')
    products = category.products
    for product in products:
        print(str(products.index(product)) + ': ' + product.name + ', ' + product.description + ', ' + str(product.price_goods) + ', ' + str(product.rating_goods))

access = False

while True:
    username = input('Введите Ваш логин: ')

    if username in users:
        access = login(username)
    else:
        access = signUp(username)

    if access == True:
        break
    else:
        print('Invalid login or pass')

while True:
    showCategories()
    while True:
        try:
            selectedCategoryIndex = int(input('Введите номер категории: '))
            if selectedCategoryIndex > len(categories) - 1:
                print("Данного номера категории не существует, повторите попытку ")
                continue
            break
        except ValueError:
            print("Некорректный ввод номера категории")
            continue

    selectedCategory = categories[selectedCategoryIndex]

    showProducts(selectedCategory)
    while True:
        try:
            selectedProductIndex = int(input('Введите номер товара: '))
            if selectedProductIndex > len(selectedCategory.products) - 1:
                print("Данного номера товара не существует, повторите попытку ")
                continue
            break
        except ValueError:
            print("Некорректный ввод номера товара")
            continue
    selectedProduct = selectedCategory.products[selectedProductIndex]

    users[username]['basket'].add(selectedProduct)

    isContinue = input('Продолжить покупки ?(N/Y): ')

    if isContinue.lower() == 'y':
        continue
    else:
        break

for item in users[username]['basket'].products:
    print(item.name)






