import random


class Product:
    name: str
    description: str
    category_ID: int

    def __init__(self, name: str, description: str, category_ID: int, price_goods: int, rating_goods: int):
        self.name = name
        self.description = description
        self.category_ID = category_ID
        self.price_goods = price_goods
        self.rating_goods = rating_goods


