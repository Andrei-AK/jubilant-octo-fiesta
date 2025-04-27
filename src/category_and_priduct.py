class Product:

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product_data: dict):
        return cls(
            name=dict_product_data["name"],
            description=dict_product_data["description"],
            price=dict_product_data["price"],
            quantity=dict_product_data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:

    name: str
    description: str
    __products: list[Product]

    total_categories = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.total_products += 1

    @property
    def products(self):
        for product in self.__products:
            print(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return self.__products
