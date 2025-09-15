import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))  # noqa: E402

from src.main import Category, Product


def test_product_initialization() -> None:
    p = Product("Имя", "Описание", 10.5, 3)
    assert p.name == "Имя"
    assert p.description == "Описание"
    assert p.price == 10.5
    assert p.quantity == 3


def test_category_initialization() -> None:
    p1 = Product("Товар1", "Описание1", 5.0, 2)
    p2 = Product("Товар2", "Описание2", 15.0, 1)
    Category.category_count = 0
    Category.product_count = 0
    c = Category("Категория1", "Описание категории", [p1, p2])
    assert c.name == "Категория1"
    assert c.description == "Описание категории"
    assert len(c.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_multiple_categories() -> None:
    Category.category_count = 0
    Category.product_count = 0
#    c1 = Category("Категория1", "Описание1", [])
#    c2 = Category("Категория2", "Описание2", [])
    assert Category.category_count == 2
    assert Category.product_count == 0
