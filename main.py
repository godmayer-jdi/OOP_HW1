from src.product import Category, Product, load_categories_from_json

if __name__ == "__main__":
    product1: Product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2: Product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3: Product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    category1: Category = Category(
        "Смартфоны",
        "Смартфоны, как средство коммуникации и для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(Category.category_count)
    print(Category.product_count)

    categories_from_json = load_categories_from_json("products.json")
    for cat in categories_from_json:
        print(f"Category {cat.name} with {len(cat.products)} products")
