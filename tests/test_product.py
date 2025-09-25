from src.product import Product, Category, CategoryIterator


def test_product_price_getter_setter():
    p = Product("Хлеб", "Свежий хлеб", 50.0, 10)
    assert p.price == 50.0

    p.price = 60.0
    assert p.price == 60.0

    # Проверка установки отрицательной цены - цена не меняется
    p.price = -10.0
    assert p.price == 60.0


def test_product_str():
    p = Product("Молоко", "Свежее", 70.5, 5)
    expected_str = "Молоко, 70.5 руб. Остаток: 5 шт."
    assert str(p) == expected_str


def test_product_add():
    p1 = Product("Молоко", "Свежее", 70, 5)  # 350
    p2 = Product("Хлеб", "Свежий", 50, 10)  # 500
    total = p1 + p2
    assert total == 850


def test_category_add_product_and_str():
    cat = Category("Продукты", "Категория продуктов")
    p1 = Product("Яблоко", "Свежие", 40, 15)
    p2 = Product("Банан", "Свежие", 60, 5)

    cat.add_product(p1)
    cat.add_product(p2)

    products_str = cat.products
    assert "Яблоко" in products_str
    assert "Банан" in products_str

    expected_str = "Продукты, количество продуктов: 20 шт."
    assert str(cat) == expected_str


def test_category_iterator():
    p1 = Product("Яблоко", "Свежие", 40, 15)
    p2 = Product("Банан", "Свежие", 60, 5)
    cat = Category("Фрукты", "Сладкие")
    cat.add_product(p1)
    cat.add_product(p2)

    # Итерация по CategoryIterator
    iter_obj = CategoryIterator(cat)
    products = list(iter_obj)
    assert products == [p1, p2]


def test_product_new_product_method():
    products_list = [Product("Яблоко", "Свежие", 40, 10)]
    new_prod_dict = {
        "name": "Яблоко",
        "description": "Зеленое",
        "price": 50,
        "quantity": 5
    }
    prod = Product.new_product(new_prod_dict, products_list)

    assert prod.quantity == 15  # Количество увеличилось
    assert prod.price == 50  # Цена обновилась, так как новая выше