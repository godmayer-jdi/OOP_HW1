from src.product import Category, CategoryIterator, Product


def test_product_str() -> None:
    p = Product("Товар", "Описание", 100, 5)
    expected = "Товар, 100 руб. Остаток: 5 шт."
    assert str(p) == expected


def test_category_str_and_products() -> None:
    p1 = Product("Яблоко", "Свежие", 50, 10)
    p2 = Product("Банан", "Спелые", 70, 5)
    cat = Category("Фрукты", "Фруктовая категория", [p1, p2])
    expected_cat_str = "Фрукты, количество продуктов: 15 шт."
    assert str(cat) == expected_cat_str

    products_str = cat.products
    assert "Яблоко, 50 руб. Остаток: 10 шт." in products_str
    assert "Банан, 70 руб. Остаток: 5 шт." in products_str


def test_product_addition() -> None:
    p1 = Product("Товар1", "Описание1", 100, 10)  # 1000
    p2 = Product("Товар2", "Описание2", 200, 2)  # 400
    assert p1 + p2 == 1400


def test_category_iterator() -> None:
    p1 = Product("Яблоко", "Свежие", 50, 10)
    p2 = Product("Банан", "Спелые", 70, 5)
    cat = Category("Фрукты", "Фруктовая категория", [p1, p2])

    iterator = CategoryIterator(cat)
    products = list(iterator)
    assert products == [p1, p2]
