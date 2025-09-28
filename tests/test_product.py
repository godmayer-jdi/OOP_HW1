import pytest

from src.product import Smartphone, LawnGrass, Category, CategoryIterator


def test_smartphone_attributes() -> None:
    sp = Smartphone("Samsung Galaxy", "256GB", 1000, 3, 95.5, "S23", 256, "Черный")
    assert sp.name == "Samsung Galaxy"
    assert sp.description == "256GB"
    assert sp.price == 1000
    assert sp.quantity == 3
    assert sp.efficiency == 95.5
    assert sp.model == "S23"
    assert sp.memory == 256
    assert sp.color == "Черный"


def test_lawngrass_attributes() -> None:
    grass = LawnGrass("Газонная трава", "Хорошая трава", 500, 7, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.description == "Хорошая трава"
    assert grass.price == 500
    assert grass.quantity == 7
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_addition_same_class() -> None:
    sp1 = Smartphone("Phone A", "desc", 100, 2, 90.0, "A1", 128, "Blue")
    sp2 = Smartphone("Phone B", "desc", 150, 3, 92.0, "B2", 256, "Black")
    result = sp1 + sp2
    expected = 100 * 2 + 150 * 3
    assert result == expected


def test_addition_different_classes_raises() -> None:
    sp = Smartphone("Phone", "desc", 100, 2, 90, "X", 128, "Blue")
    grass = LawnGrass("Трава", "desc", 50, 10, "Россия", "5 дней", "Зеленый")
    with pytest.raises(TypeError):
        _ = sp + grass


def test_add_product_valid_and_invalid() -> None:
    cat = Category("Категория", "Описание")

    sp = Smartphone("Phone X", "desc", 120, 1, 90, "X", 128, "Серый")
    grass = LawnGrass("Газон", "desc", 40, 5, "Россия", "6 дней", "Зеленый")

    cat.add_product(sp)
    cat.add_product(grass)

    assert len(cat.product_list) == 2

    with pytest.raises(TypeError):
        cat.add_product("not a product")  # type: ignore[arg-type]


def test_category_str_and_products() -> None:
    sp = Smartphone("Phone S", "desc", 200, 1, 95, "S", 256, "Белый")
    grass = LawnGrass("Газон 2", "desc", 30, 10, "США", "4 дня", "Темно-зеленый")

    cat = Category("Продукты", "Описание", [sp, grass])
    out_str = str(cat)
    assert "Продукты" in out_str
    assert "количество продуктов" in out_str

    products_str = cat.products
    assert "Phone S" in products_str
    assert "Газон 2" in products_str


def test_category_iterator() -> None:
    sp = Smartphone("Phone S", "desc", 200, 1, 95, "S", 256, "Белый")
    grass = LawnGrass("Газон 2", "desc", 30, 10, "США", "4 дня", "Темно-зеленый")
    cat = Category("Продукты", "Описание", [sp, grass])

    iterator = CategoryIterator(cat)
    products = list(iterator)
    assert products == [sp, grass]