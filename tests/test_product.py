import pytest
from classes import Product


@pytest.fixture
def product():
    return Product(name='Хлеб', price=10, quantity=5, description="товар")


def test_init(product):
    assert product.name == 'Хлеб'
    assert product.price == 10
    assert product.quantity == 5
    assert product.description == "товар"


def test_price(product):
    price = 15
    # установка новой цены
    product.price = price
    assert product.price == price
    # нулевая цена
    with pytest.raises(Exception):
        product.price = 0


def test_create(product):
    title = 'яблоко'
    price = 11.5
    count = 3
    description = 'фрукт'
    product = Product.create({'name': title, 'price': price, 'quantity': count, 'description': description})
    assert product.name == title
    assert product.price == price
    assert product.quantity == count
    assert product.description == description
