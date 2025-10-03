import pytest
from src.product import Product, Category, ZeroQuantityError


def test_product_zero_quantity() -> None:
    with pytest.raises(ZeroQuantityError) as exc:
        Product("NoQty", "desc", 10, 0)
    assert str(exc.value) == "Товар с нулевым количеством не может быть добавлен"


def test_category_average_price() -> None:
    p1 = Product("p1", "desc", 50, 1)
    p2 = Product("p2", "desc", 100, 1)
    cat = Category("cat", "desc", [p1, p2])
    assert cat.middle_price() == 75.0

    empty_cat = Category("empty", "desc", [])
    assert empty_cat.middle_price() == 0.0
