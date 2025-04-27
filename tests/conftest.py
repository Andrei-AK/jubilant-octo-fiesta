import pytest

from src.category_and_priduct import Category, Product


@pytest.fixture
def some_product() -> Product:
    return Product("Ноутбук", "Игровой", 50000.0, 10)


@pytest.fixture
def some_category(some_product) -> Category:
    Category.total_categories = 0
    Category.total_products = 0

    return Category("Электроника", "Техника", [some_product])
