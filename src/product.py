from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class ZeroQuantityError(ValueError):
    """Исключение для товара с нулевым количеством."""

    pass


class BaseProduct(ABC):
    """
    Абстрактный базовый класс, задаёт общие атрибуты и интерфейс продукта.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass


class PrintInfoMixin:
    """
    Миксин, выводит информацию о создаваемом экземпляре.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        cls_name = self.__class__.__name__
        print(f"Создан объект класса {cls_name} с аргументами: args={args}, kwargs={kwargs}")
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class Product(PrintInfoMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        if quantity == 0:
            raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
        self.__price = price
        super().__init__(name, description, price, quantity)

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
        if type(self) is not type(other):
            raise TypeError("Сложение возможно только между объектами одного класса")
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


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: Optional[List[Product]] = None,
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self) -> float:
        try:
            if len(self.__products) == 0:
                return 0.0
            total_price = sum(prod.price for prod in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    @property
    def products(self) -> str:
        return "".join(str(prod) + "\n" for prod in self.__products)

    @property
    def product_list(self) -> List[Product]:
        return self.__products

    def __str__(self) -> str:
        total_quantity = sum(prod.quantity for prod in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
