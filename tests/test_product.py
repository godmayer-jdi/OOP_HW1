from src.product import Product, Category


def test_add_product_and_getter():
    cat = Category("Фрукты", "Фрукты и ягоды")
    p1 = Product("Яблоко", "Свежие", 50, 10)
    p2 = Product("Банан", "Спелые", 70, 5)
    cat.add_product(p1)
    cat.add_product(p2)

    products_str = cat.products

    assert "Яблоко, 50 руб. Остаток: 10 шт." in products_str
    assert "Банан, 70 руб. Остаток: 5 шт." in products_str
    assert Category.product_count >= 2


def test_price_setter_rejects_non_positive():
    p = Product("Молоко", "Свежие", 100, 20)

    old_price = p.price
    p.price = 0  # должна остаться старая цена
    assert p.price == old_price

    p.price = -10  # тоже должна остаться старая цена
    assert p.price == old_price


def test_price_setter_allows_price_decrease(monkeypatch):
    p = Product("Молоко", "Свежие", 100, 20)

    # Симулируем ввод 'y' для подтверждения снижения цены
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 80
    assert p.price == 80

    # Симулируем ввод 'n' для отмены снижения цены
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 50
    assert p.price == 80  # цена не изменилась


def test_new_product_and_duplicates():
    products = [
        Product("Хлеб", "Черный хлеб", 30, 5),
        Product("Масло", "Сливочное", 150, 2),
    ]

    new_prod_dict = {"name": "Хлеб", "price": 40, "description": "Белый хлеб", "quantity": 10}
    prod = Product.new_product(new_prod_dict, products)

    # Количество сложилось
    assert prod.quantity == 15
    # Цена выбрана максимальная из двух
    assert prod.price == 40

    new_prod_dict2 = {"name": "Сок", "price": 90, "description": "Апельсиновый", "quantity": 4}
    prod2 = Product.new_product(new_prod_dict2, products)
    assert prod2.name == "Сок"
    assert prod2.quantity == 4
    # Проверяем, что новый продукт не добавился в исходный список напрямую
    assert len(products) == 2