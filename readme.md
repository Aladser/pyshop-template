# Шаблон интернет-магазина

+ ``src``
    * ``Product`` - класс продукта
    * ``Category`` - класс категории.  Список продуктов - список элементов класса Product
    * ``CategoryProductRange`` - итератор продуктов категории
+ ``tests``
    * ``test_product`` - тест пррдукта
    * ``test_category`` - тест категории
    * `test_ctgprd_iterator` - тест итератора продуктов категории
+ ``load_data.py`` - парсинг JSON файла и выгрузка категорий и товаров из него.
