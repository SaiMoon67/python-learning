prices = {"хлеб": 50, "молоко": 90, "сыр": 400}
product = input("Введите название товара: ").lower()
price = prices.get(product)
if price is None:
    print("Такого товара нет")
else:
    print(price)
