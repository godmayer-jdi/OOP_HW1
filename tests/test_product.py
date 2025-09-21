from src.product import Category, Product


def test_add_product_and_getter() -> None:
    cat = Category("Фрукты", "Фрукты и ягоды")
    p1 = Product("Яблоко", "Свежие", 50, 10)
    p2 = Product("Банан", "Спелые", 70, 5)
    cat.add_product(p1)
    cat.add_product(p2)

    products_str = cat.products

    assert "Яблоко, 50 руб. Остаток: 10 шт." in products_str
    assert "Банан, 70 руб. Остаток: 5 шт." in products_str
    assert Category.product_count >= 2


def test_price_setter_rejects_non_positive() -> None:
    p = Product("Молоко", "Свежие", 100, 20)

    old_price = p.price
    p.price = 0  # Цена не изменится
    assert p.price == old_price

    p.price = -10  # Цена не изменится
    assert p.price == old_price


def test_price_setter_allows_price_decrease_without_input() -> None:
    p = Product("Молоко", "Свежие", 100, 20)
    p.set_price(80, confirm=False)
    assert p.price == 80


def test_new_product_and_duplicates() -> None:
    products = [
        Product("Хлеб", "Черный хлеб", 30, 5),
        Product("Масло", "Сливочное", 150, 2),
    ]

    new_prod_dict = {"name": "Хлеб", "price": 40, "description": "Белый хлеб", "quantity": 10}
    prod = Product.new_product(new_prod_dict, products)

    assert prod.quantity == 15
    assert prod.price == 40

    new_prod_dict2 = {"name": "Сок", "price": 90, "description": "Апельсиновый", "quantity": 4}
    prod2 = Product.new_product(new_prod_dict2, products)
    assert prod2.name == "Сок"
    assert prod2.quantity == 4
    assert len(products) == 2
