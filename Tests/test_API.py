import allure
import pytest
from API.ChitaiGorod_collection import CG_API
from specific_data import API_URL, token, product_json, product_id, quantity_json, book_title


chitai_gorod = CG_API(API_URL, token)
chitai_gorod_unauthorized = CG_API(API_URL, '')




@allure.title('Добавление книги в корзину')
@allure.description('')
@allure.feature('Корзина')
@allure.severity('S2')
@pytest.mark.API
def test_add_to_cart_positive():
    with allure.step('Отправить запрос на добавление товара в корзину'):
        response = chitai_gorod.add_to_cart(product_json)

    with allure.step('Статус код 200'):
        assert response.status_code == 200

    with allure.step('Проверить что книга добавлена в корзину'):
        response = chitai_gorod.get_cart()
        assert response.json()['products'][0]['title'] == book_title
        chitai_gorod.remove_from_cart(product_id)




@allure.title('Изменение количества товара в корзине')
@allure.description('')
@allure.feature('Корзина')
@allure.severity('S2')
@pytest.mark.API
def test_change_quantity_positive():
    with allure.step('Отправить запрос на добавление товара в корзину'):
        chitai_gorod.add_to_cart(product_json)

    with allure.step('Изменить количество товара в корзине'):
        response = chitai_gorod.change_quantity_cart(quantity_json)

    with allure.step('Статус код 200'):
        assert response.status_code == 200

    with allure.step('Проверить что количество товара изменилось'):
        response = chitai_gorod.get_cart()
        assert response.json()['products'][0]['quantity'] == 2
        chitai_gorod.remove_from_cart(product_id)




@allure.title('Удаление товара из корзины')
@allure.description('')
@allure.feature('Корзина')
@allure.severity('S2')
@pytest.mark.API
def test_remove_from_cart_positive():
    with allure.step('Отправить запрос на добавление товара в корзину'):
        chitai_gorod.add_to_cart(product_json)

    with allure.step('Отправить запрос на удаление товара из корзины'):
        response = chitai_gorod.remove_from_cart(product_id)

    with allure.step('Статус код 204'):
        assert response.status_code == 204

    with allure.step('Проверить что товар удален'):
        response = chitai_gorod.get_cart()
        assert len(response.json()['products']) == 0




@allure.title('Добавление книги в корзину без токена авторизации')
@allure.description('')
@allure.feature('Корзина')
@allure.severity('S2')
@pytest.mark.API
def test_add_to_cart_unauthorized_negative():
    with allure.step('Отправить запрос на добавление товара в корзину без токена авторизации'):
        response = chitai_gorod_unauthorized.add_to_cart(product_json)

    with allure.step('Статус код 401'):
        assert response.status_code == 401




@allure.title('Изменение количества товара в корзине без токена авторизации')
@allure.description('')
@allure.feature('Корзина')
@allure.severity('S2')
@pytest.mark.API
def test_change_quantity_unauthorized_negative():
    with allure.step('Отправить запрос на изменение количества товара в корзину без токена авторизации'):
        response = chitai_gorod_unauthorized.change_quantity_cart(quantity_json)

    with allure.step('Статус код 401'):
        assert response.status_code == 401




@allure.title('Удаление товара из корзины без токена авторизации')
@allure.description('')
@allure.feature('Корзина')
@allure.severity('S2')
@pytest.mark.API
def test_remove_from_cart_unauthorized_negative():
    with allure.step('Отправить запрос на удаление товара из корзины без токена авторизации'):
        response = chitai_gorod_unauthorized.remove_from_cart(product_id)

    with allure.step('Статус код 401'):
        assert response.status_code == 401
