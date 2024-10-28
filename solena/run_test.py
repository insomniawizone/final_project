from solena.step import *

#pytest solena/run_test.py --html=solena/report.html -v
@pytest.mark.smoke  # имитация поведения пользователя во время навигации по сайту
def test_potential_path(page: Page, potential_path):
    """Проверка входа"""
    potential_path()

@pytest.mark.smoke  # проверка функции "Заказать прайс"
def test_get_price(page: Page, get_price):
    """Проверка входа"""
    get_price()

@pytest.mark.smoke  # проверка функции "Узнать цену"
def test_know_price(page: Page, know_price):
    """Проверка входа"""
    know_price()

@pytest.mark.smoke  # проверка функции "Рассчитаем ваш заказ"
def test_price_count(page: Page, price_count):
    """Проверка входа"""
    price_count()

@pytest.mark.smoke  # проверка функции "Заказать расчет"
def test_order_price(page: Page, order_price):
    """Проверка входа"""
    order_price()