"""
Модуль для работы с товарами для строительного магазина
"""


class Goods:

    def __init__(self, code_goods: int, name_goods: str, preis_goods: float, rating_goods: float):

        if not isinstance(code_goods, int):
            raise TypeError("Некорректный тип данных в коде товара ")
        if code_goods < 0:
            raise ValueError("Некорректное значение кода товара ")

        self.code_goods = code_goods
        self.name_goods = name_goods
        self.preis_goods = preis_goods
        self.rating_goods = rating_goods


goods_1 = Goods
print(goods_1)

if __name__ == "__main__":
    goods_1 = Goods(111, "дрель_1", 120.5, 8.0)
    goods_2 = Goods(112, "дрель_2", 119.9, 4.9)

print(goods_1)
print(goods_2)



from dataclasses import dataclass, field


@dataclass
class Goods():
    code_goods: int = None
    name_goods: str = field(default_factory=str)
    preis_goods: float = 0
    rating_goods: float = 0

goods = Goods()

drill = Goods(111, "дрель", 100.0, 4.5)
print(drill)
