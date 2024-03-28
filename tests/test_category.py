import pytest
from classes import Category, Product


@pytest.fixture
def title():
    return 'еда'


@pytest.fixture
def description():
    return 'здесь должна быть реклама'


@pytest.fixture
def products():
    return [
        Product(title='Хлеб', price=5, count=1, description='Товар 1'),
        Product(title='Чай', price=15, count=3, description='Товар 2'),
        Product(title='Сахар', price=20, count=4, description='Товар 3')
    ]


@pytest.fixture
def category(title, products, description):
    return Category(title, products, description)


def test_products(category):
    assert Category.products_count == 3


def test_count_categories(category):
    # в таком случае неизбежно создается 2 экземпляра
    assert Category.count == 2


def test_init(category, title, products, description):
    assert category.title == title
    assert category.description == description


def test_add(category):
    product = Product(title='Батон', price=5, count=1, description='Товар 4')
    category.add_product(product)
    # добавить
    assert Category.products_count == 13
    assert category.products[3].split(' ')[1] == '5'
    # повысить цену
    product = Product(title='Батон', price=10, count=1, description='Товар 4')
    category.add_product(product)
    assert category.products[3].split(' ')[1] == '10'
    # понизить цену
    product = Product(title='Батон', price=4, count=1, description='Товар 4')
    category.add_product(product)
    assert category.products[3].split(' ')[1] == '10'