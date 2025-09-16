import json
from typing import List


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products

        Category.category_count += 1
        Category.product_count += len(products)


def load_categories_from_json(filepath: str) -> List[Category]:
    categories: List[Category] = []
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
        Category.category_count = 0
        Category.product_count = 0

        for category_data in data:
            products: List[Product] = []
            for product_data in category_data.get("products", []):
                product = Product(
                    name=product_data["name"],
                    description=product_data["description"],
                    price=product_data["price"],
                    quantity=product_data["quantity"],
                )
                products.append(product)
            category = Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
            categories.append(category)
    return categories
