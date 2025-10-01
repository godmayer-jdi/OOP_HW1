import pytest

from src.product import Category, Product


def test_product_creation_and_str() -> None:
    p = Product("Test", "Test product", 100.0, 5)
    assert p.name == "Test"
    assert p.description == "Test product"
    assert p.price == 100.0
    assert p.quantity == 5
    assert str(p) == "Test, 100.0 руб. Остаток: 5 шт."


def test_product_total_price_and_add() -> None:
    p1 = Product("P1", "Desc", 100.0, 2)
    p2 = Product("P2", "Desc", 200.0, 3)
    assert p1.total_price() == 200.0
    assert p2.total_price() == 600.0

    # Сложение продуктов
    total = p1 + p2
    assert total == 800.0

    with pytest.raises(TypeError):
        _ = p1 + "not a product"  # type: ignore


def test_category_and_add_product() -> None:
    p1 = Product("P1", "Desc", 100, 1)
    p2 = Product("P2", "Desc", 200, 2)
    cat = Category("Cat", "Description", [p1])
    assert cat.name == "Cat"
    assert cat.description == "Description"
    assert len(cat.products) == 1
    assert Category.category_count > 0

    cat.add_product(p2)
    assert len(cat.products) == 2
    assert Category.product_count >= 2

    with pytest.raises(TypeError):
        cat.add_product("no product")  # type: ignore


def test_category_str() -> None:
    p1 = Product("P1", "Desc", 5, 3)
    p2 = Product("P2", "Desc", 10, 2)
    cat = Category("Name", "Desc", [p1, p2])
    expected = "Name, количество продуктов: 5 шт."
    assert str(cat) == expected
