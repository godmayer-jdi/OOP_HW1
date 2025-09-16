import json
from pathlib import Path
from typing import List

from src.product import Category, Product, load_categories_from_json


def test_product_init() -> None:
    p = Product("Test", "Desc", 100.0, 5)
    assert p.name == "Test"
    assert p.description == "Desc"
    assert p.price == 100.0
    assert p.quantity == 5


def test_category_init_and_counters() -> None:
    Category.category_count = 0
    Category.product_count = 0

    p1: Product = Product("P1", "Desc1", 10.0, 1)
    p2: Product = Product("P2", "Desc2", 20.0, 2)
    c: Category = Category("Cat1", "Category 1", [p1, p2])

    assert c.name == "Cat1"
    assert c.description == "Category 1"
    assert len(c.products) == 2

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_load_categories_from_json(tmp_path: Path) -> None:
    data: List[dict] = [
        {
            "name": "CatJSON",
            "description": "Cat Desc",
            "products": [
                {"name": "J1", "description": "DescJ1", "price": 1.0, "quantity": 1},
                {"name": "J2", "description": "DescJ2", "price": 2.0, "quantity": 2},
            ],
        }
    ]
    file: Path = tmp_path / "categories.json"
    file.write_text(json.dumps(data), encoding="utf-8")

    categories: List[Category] = load_categories_from_json(str(file))

    assert len(categories) == 1
    c: Category = categories[0]
    assert c.name == "CatJSON"
    assert c.description == "Cat Desc"
    assert len(c.products) == 2

    assert isinstance(c.products[0], Product)
    assert c.products[0].name == "J1"
    assert c.products[0].price == 1.0

    assert Category.category_count == 1
    assert Category.product_count == 2
