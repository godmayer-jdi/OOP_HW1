import pytest
from src.product import Product, Smartphone, LawnGrass, Category


def test_product_creation() -> None:
    p = Product("Test", "Test product", 100.0, 5)
    assert p.name == "Test"
    assert p.description == "Test product"
    assert p.price == 100.0
    assert p.quantity == 5
    assert str(p) == "Test, 100.0 руб. Остаток: 5 шт."


def test_product_set_price_and_addition() -> None:
    p1 = Product("Prod1", "Desc", 50.0, 2)
    p2 = Product("Prod2", "Desc", 70.0, 3)
    assert p1.price == 50.0
    p1.set_price(60.0, confirm=False)
    assert p1.price == 60.0
    total = p1 + p2
    assert total == (60.0 * 2 + 70.0 * 3)

    with pytest.raises(TypeError):
        _ = p1 + "not a product"  # type: ignore


def test_smartphone_attributes() -> None:
    sp = Smartphone("Samsung", "Phone", 1000, 1, 95.5, "S23 Ultra", 256, "Серый")
    assert sp.name == "Samsung"
    assert sp.efficiency == 95.5
    assert sp.model == "S23 Ultra"
    assert sp.memory == 256
    assert sp.color == "Серый"
    s = str(sp)
    assert "Samsung" in s


def test_lawngrass_attributes() -> None:
    grass = LawnGrass("Газон", "Трава", 300, 10, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Газон"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"
    s = str(grass)
    assert "Газон" in s


def test_category_basic_operations() -> None:
    p1 = Product("Prod1", "Desc", 100, 1)
    p2 = Product("Prod2", "Desc", 200, 2)
    cat = Category("Категория", "Описание", [p1])
    assert cat.name == "Категория"
    assert cat.description == "Описание"
    assert len(cat.products) == 1
    assert Category.category_count > 0

    cat.add_product(p2)
    assert len(cat.products) == 2
    assert Category.product_count >= 2

    with pytest.raises(TypeError):
        cat.add_product("не продукт")  # type: ignore


def test_category_str_representation() -> None:
    p1 = Product("Prod1", "Desc", 5, 3)
    p2 = Product("Prod2", "Desc", 15, 2)
    cat = Category("Категория", "Описание", [p1, p2])
    expected = "Категория, количество продуктов: 5 шт."
    assert str(cat) == expected
