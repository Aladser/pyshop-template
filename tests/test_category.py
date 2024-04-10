import pytest
from classes import Category, Product, Grass


class TestCls:
    pass


@pytest.fixture
def products():
    return [
        Product(name='Хлеб', price=5, quantity=12, description='Товар 1')
    ]


@pytest.fixture
def category(products):
    return Category('еда', 'здесь должна быть реклама', products)


def test_init(category, products):
    assert category.name == 'еда'
    assert category.description == 'здесь должна быть реклама'
    assert category.products == [str(prd) for prd in products]
    assert Category.products_quantity == 1
    assert Category.quantity == 1
    assert len(category) == 12
    assert category.products == ['Хлеб, 5 руб. Остаток: 12 шт.']


def test_work(category):
    bread = Product(name='Хлеб', price=5, quantity=1, description='Товар 1')
    params = {
        'name': 'газонная',
        'description': 'городская',
        'price': 10,
        'quantity': 1,
        'country_manufacturer': 'Россия',
        'germination_period': '1 year',
        'color': 'зеленый'
    }
    grass = Grass(**params)

    # добавление товара
    category.add_product(bread)
    assert Category.products_quantity == 2
    category.add_product(grass)
    assert Category.products_quantity == 3
    with pytest.raises(Exception):
        category.add_product(TestCls())
    # дубль товара
    category.add_product(bread)
    assert Category.products_quantity == 3