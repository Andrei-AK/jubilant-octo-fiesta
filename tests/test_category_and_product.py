from src.category_and_priduct import Category, Product


def test_product_init(some_product):
    assert some_product.name == "Ноутбук"
    assert some_product.description == "Игровой"
    assert some_product.price == 50000.0
    assert some_product.quantity == 10


def test_category_init(some_product, some_category):
    assert some_category.name == "Электроника"
    assert some_category.description == "Техника"
    assert len(some_category.products) == 1
    assert some_category.products[0] == some_product

    assert Category.total_categories == 1
    assert Category.total_products == 1


def test_new_product(some_product):
    test_data = {"name": "Наушники", "description": "Беспроводные", "price": 15000.0, "quantity": 8}
    product = Product.new_product(test_data)
    assert product.name == "Наушники"
    assert product.price == 15000.0
    assert product.quantity == 8


def test_price_setter(some_product):
    product = some_product
    product.price = 5000
    assert product.price == 5000


def test_price_getter(some_product):
    assert some_product.price == 50000.0


def test_add_product(some_product):
    category = Category("test_category", "test_description", [])
    category.add_product(some_product)
    assert len(category.products) == 1


def test_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    assert len(category1.products) == 3
    assert category1.products[0].name == "Samsung Galaxy S23 Ultra"
    assert category1.products[1].name == "Iphone 15"
    assert category1.products[2].name == "Xiaomi Redmi Note 11"
