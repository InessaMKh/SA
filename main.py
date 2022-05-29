from hardware_store.product import Product





import random

name_goods = ["дрель", "шуруповерт", "бензопила", "бетономешалка"]
descriptions = ["железный", "пластик", "горючий", "круглый"]
categoriesID = [123, 456, 789, 987]
products = []

for i in range(0, 9):
    name = name_goods[random.randint(0, (len(name_goods)-1))]
    description = descriptions[random.randint(0, (len(descriptions) -1))]
    categoryID = categoriesID[random.randint(0, (len(categoriesID) -1))]

    products.append(Product(name, description, categoryID))


#products_ = Product
print(products)







