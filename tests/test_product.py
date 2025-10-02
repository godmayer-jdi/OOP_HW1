import pytest
from pytest import CaptureFixture

from src.product import Category, LawnGrass, Product, Smartphone


def test_product_creation_and_str() -> None:
    p = Product("TestProduct", "Test Description", 100.0, 10)
    assert p.name == "TestProduct"
    assert p.description == "Test Description"
    assert p.price == 100.0
    assert p.quantity == 10
    assert str(p) == "TestProduct, 100.0 руб. Остаток: 10 шт."


def test_print_info_mixin_output(capfd: CaptureFixture[str]) -> None:
    _ = Product("MixinTest", "Desc", 50.0, 5)
    out, _ = capfd.readouterr()
    assert "Создан объект класса Product с аргументами" in out


def test_set_price_and_price_setter() -> None:
    p = Product("PriceTest", "Desc", 100.0, 1)
    p.set_price(80.0, confirm=False)
    assert p.price == 80.0
    p.price = 90.0
    assert p.price == 90.0

    # Price <= 0 should be ignored
    p.set_price(-10, confirm=False)
    assert p.price == 90.0


def test_addition_of_products_and_type_error() -> None:
    p1 = Product("P1", "Desc", 100.0, 1)
    p2 = Product("P2", "Desc", 200.0, 2)
    assert p1 + p2 == 100.0 * 1 + 200.0 * 2

    sp = Smartphone("S1", "Smartphone", 300.0, 1, 90.5, "S Model", 128, "Black")

    with pytest.raises(TypeError):
        _ = p1 + sp  # different classes


def test_smartphone_attributes_and_str() -> None:
    sp = Smartphone("PhoneX", "Desc", 1500.0, 3, 95.0, "ModelX", 256, "White")
    assert sp.name == "PhoneX"
    assert sp.efficiency == 95.0
    assert sp.memory == 256
    s = str(sp)
    assert "PhoneX" in s


def test_lawngrass_attributes_and_str() -> None:
    grass = LawnGrass("Grass", "Desc", 20.0, 100, "Russia", "7 days", "Green")
    assert grass.country == "Russia"
    s = str(grass)
    assert "Grass" in s


def test_category_add_product_and_counts() -> None:
    p1 = Product("P1", "Desc", 100, 1)
    p2 = Product("P2", "Desc", 150, 2)
    category = Category("Category1", "Desc", [p1])
    assert category.name == "Category1"
    assert len(category.product_list) == 1

    category.add_product(p2)
    assert len(category.product_list) == 2

    with pytest.raises(TypeError):
        category.add_product("Not a product")  # type: ignore


def test_category_str_and_products_property() -> None:
    p1 = Product("P1", "Desc", 10, 1)
    p2 = Product("P2", "Desc", 15, 2)
    cat = Category("CatName", "Desc", [p1, p2])
    s = str(cat)
    assert "CatName" in s
    assert "количество продуктов" in s
    products_str = cat.products
    assert "P1" in products_str
    assert "P2" in products_str
