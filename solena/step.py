from solena.config import *
from solena.data import *
from solena.locator import *


@pytest.fixture
def get_price(page: Page):
    def get_price_function():
        page.goto("https://pksolena.ru")
        page.wait_for_timeout(2000)
        page.click(locator_get_price)
        page.wait_for_timeout(1000)
        page.fill(locator_get_price_name, data_name)
        page.fill(locator_get_price_number, data_number)
        page.fill(locator_get_price_email,data_email)
        page.fill(locator_get_price_org,data_org)
        page.fill(locator_get_price_kg,data_kg)
        page.wait_for_timeout(1000)
        page.click(locator_get_price_extra_salt)
        page.wait_for_timeout(2000)
        page.click(locator_get_price_submit)
        page.wait_for_timeout(2000)
        page.screenshot(path='screen/get_price.png')
    return get_price_function

@pytest.fixture
def know_price(page: Page):
    def know_price_function():
        page.goto("https://pksolena.ru")
        page.wait_for_timeout(2000)
        page.click(locator_know_price_best)
        page.wait_for_timeout(1000)
        page.fill(locator_know_price_best_name, data_name)
        page.fill(locator_know_price_best_number, data_number)
        page.fill(locator_know_price_best_email, data_email)
        page.fill(locator_know_price_best_org, data_org)
        page.wait_for_timeout(2000)
        page.click(locator_know_price_best_delete_all)
        page.wait_for_timeout(1000)
        page.click(locator_know_price_best_return_item_timer)
        page.wait_for_timeout(1000)
        page.click(locator_know_price_best_submit_button)
        page.wait_for_timeout(2000)
        page.screenshot(path='screen/know_price.png')
    return know_price_function

@pytest.fixture
def price_count(page: Page):
    def price_count_function():
        page.goto("https://pksolena.ru")
        page.wait_for_timeout(2000)
        page.fill(locator_last_field_name, data_name)
        page.fill(locator_last_field_number,data_number)
        page.fill(locator_last_field_commentary, data_commentary)
        page.wait_for_timeout(1000)
        page.click(locator_last_button_send)
        page.wait_for_timeout(2000)
        page.screenshot(path='screen/price_count.png')
    return price_count_function

@pytest.fixture
def order_price(page: Page):
    def order_price_function():
        page.goto("https://pksolena.ru")
        page.wait_for_timeout(2000)
        page.click(locator_order_button)
        page.wait_for_timeout(1000)
        page.fill(locator_order_name, data_name)
        page.fill(locator_order_number, data_number)
        page.fill(locator_order_email, data_email)
        page.fill(locator_order_org, data_org)
        page.fill(locator_order_kg, data_kg)
        page.wait_for_timeout(1000)
        page.click(locator_order_extra_salt)
        page.wait_for_timeout(1000)
        page.click(locator_order_order_submit)
        page.wait_for_timeout(2000)
        page.screenshot(path='screen/order_price.png')
    return order_price_function

@pytest.fixture
def potential_path(page: Page):
    def potential_path_function():
        page.goto("https://pksolena.ru")
        page.wait_for_timeout(2000)
        page.click(locator_about_us)
        page.wait_for_timeout(1000)
        page.click(locator_delivery)
        page.wait_for_timeout(1000)
        page.click(locator_sertificate)
        page.wait_for_timeout(1000)
        page.click(locator_sertificate1)
        page.wait_for_timeout(1000)
        page.click(locator_sertificate_next)
        page.click(locator_sertificate_next)
        page.wait_for_timeout(1000)
        page.click(locator_sertificate_close)
        page.click(locator_sertificate4)
        page.wait_for_timeout(1000)
        page.click(locator_sertificate_close)
        page.wait_for_timeout(1000)
        page.click(locator_photos_forward)
        page.click(locator_photos_forward)
        page.wait_for_timeout(1000)
        page.click(locator_photos_forward)
        page.wait_for_timeout(1000)
        page.click(locator_photos_back)
        page.wait_for_timeout(1000)
        page.click(locator_photos_back)
        page.click(locator_articles)
        page.wait_for_timeout(1000)
        page.click(locator_contact_us)
        page.wait_for_timeout(1000)
        page.click(locator_yandex_maps_zoomin)
        page.wait_for_timeout(1000)
        page.click(locator_yandex_maps_zoomout)
        page.hover(locator_catalog)
        page.click(locator_food_salt)
        page.wait_for_timeout(1000)
        page.hover(locator_catalog2)
        page.click(locator_lizunets)
        page.wait_for_timeout(1000)
        page.hover(locator_catalog2)
        page.click(locator_galit)
        page.wait_for_timeout(1000)
        page.hover(locator_catalog2)
        page.click(locator_soda)
        page.wait_for_timeout(1000)
        page.click(locator_get_price_salt)
        page.wait_for_timeout(1000)
        page.fill(locator_get_price_salt_name, data_name)
        page.fill(locator_get_price_salt_phone, data_number)
        page.fill(locator_get_price_salt_email, data_email)
        page.fill(locator_get_price_salt_org, data_org)
        page.fill(locator_get_price_salt_kg, data_kg)
        page.wait_for_timeout(1000)
        page.click(locator_get_price_salt_submit)
        page.wait_for_timeout(2000)
        page.screenshot(path='screen/get_price_salt.png')
    return potential_path_function