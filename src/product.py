from abc import ABC, abstractmethod
from typing import List, Optional


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для продукта.
    Содержит общие свойства и методы, обязательные для реализации во всех продуктах.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """
        Строковое представление продукта.
        """
        pass

    @abstractmethod
    def total_price(self) -> float:
        """
        Общая стоимость товара с учётом количества.
        """
        pass


class PrintInfoMixin:
    """
    Миксин, который при создании объекта выводит информацию о классе и аргументах.
    """

    def __init__(self, *args, **kwargs) -> None:
        cls_name = self.__class__.__name__
        print(f"Создан объект класса {cls_name} с аргументами: args={args}, kwargs={kwargs}")
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class Product(PrintInfoMixin, BaseProduct):
    """
    Класс продукта, наследует общий абстрактный продукт и миксин для печати информации.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def total_price(self) -> float:
        return self.price * self.quantity

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Можно складывать только объекты одного класса")
        return self.total_price() + other.total_price()


class Category:
    """
    Класс категории, хранит продукты и их количество, имеет имя и описание.
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(
        self, name: str, description: str, products: Optional[List[Product]] = None
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        return self.__products

    def __str__(self) -> str:
        total_quantity = sum(prod.quantity for prod in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
