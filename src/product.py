import json
from typing import Any, Dict, List, Optional


class Product:
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name = name
        self.description = description
        self._price = price  # приватный атрибут цены
        self.quantity = quantity

    def set_price(self, new_price: float, confirm: bool = True) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if confirm and new_price < self._price:
            answer = input(f"Цена понижается с {self._price} до {new_price}. Подтвердить (y/n)? ")
            if answer.lower() != "y":
                return
        self._price = new_price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        # При обычном использовании вызываем с подтверждением
        self.set_price(new_price, confirm=True)

    @classmethod
    def new_product(
        cls,
        product_dict: Dict[str, Any],
        products_list: Optional[List["Product"]] = None,
    ) -> "Product":
        name = product_dict.get("name")
        if not isinstance(name, str):
            raise ValueError("Product name must be a string and cannot be None")
        description = product_dict.get("description", "")
        price = product_dict.get("price", 0)
        quantity = product_dict.get("quantity", 0)

        if products_list is not None:
            for prod in products_list:
                if prod.name == name:
                    prod.quantity += quantity
                    if price > prod.price:
                        prod.set_price(price, confirm=False)  # тестовый вызов без подтверждения
                    return prod
        return cls(name, description, price, quantity)


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "".join(f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n" for prod in self.__products)


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
