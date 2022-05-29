"""
Модуль для работы с корзиной покупаителя строительного магазина
"""


class Basket:
    products = []

    def add(self, product):
        self.products.append(product)

    def remove(self, product):
        self.products.remove(product)

