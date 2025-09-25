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
        self.__price = price  # приватный атрибут с двойным подчёркиванием
        self.quantity = quantity

    def set_price(self, new_price: float, confirm: bool = True) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if confirm and new_price < self.__price:
            answer = input(f"Цена понижается с {self.__price} до {new_price}. Подтвердить (y/n)? ")
            if answer.lower() != "y":
                return
        self.__price = new_price

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        self.set_price(new_price, confirm=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            return NotImplemented
        return (self.price * self.quantity) + (other.price * other.quantity)

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
                        prod.set_price(price, confirm=False)
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
        return "".join(str(prod) + "\n" for prod in self.__products)

    @property
    def product_list(self) -> List[Product]:
        # Публичный геттер для доступа к списку продуктов (для итератора)
        return self.__products

    def __str__(self) -> str:
        total_quantity = sum(prod.quantity for prod in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


class CategoryIterator:
    def __init__(self, category: Category) -> None:
        self._products = category.product_list  # доступ через публичный геттер
        self._index = 0

    def __iter__(self) -> "CategoryIterator":
        return self

    def __next__(self) -> Product:
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration()
