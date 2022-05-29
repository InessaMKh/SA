"""
Модуль работы с категориями товаров строительного магазина
"""
import random
from hardware_store.product import Product


class Category:
    title: str
    products: list

    def __init__(self, title):
        self.title = title
        self.products = []

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.append(product)


categoriesTitles = ['Инструменты', 'Оборудование', "Материалы", "Техника"]
categories = []

for title in categoriesTitles:
    categories.append(Category(title))

name_goods_0 = ["дрель", "шуруповерт", "молоток", "топор", "гвозди", "шурупы", "саморезы", ",бензопила", "бетономешалка", "газонокосилка", "песок", "бетон", "плитка тратуарная", "шифер"]
descriptions_0 = ["железный", "пластиковый", "металический", "чугунный"]

for category in categories:
    for i in range(0, 10):
        name = name_goods_0[random.randint(0, (len(name_goods_0) - 1))]
        description = descriptions_0[random.randint(0, (len(descriptions_0) - 1))]
        price = random.randint(100, 200)
        rating = random.randint(3, 6)
        categoryID = category.title

        category.add(Product(name, description, categoryID, price, rating))

