import allure
import requests

import helpers
from data import TestData, Message


@allure.story('Тесты получения заказов пользователя')
class TestGetUserOrders:
    @allure.title('Тест получения заказа авторизированным пользователем')
    def test_get_orders_authorized_user(self, user):
        helpers.create_order(TestData.INGREDIENT, user['json']['accessToken'])
        response = helpers.get_user_orders(user['json']['accessToken'])
        assert (response.status_code == 200 and
                (TestData.INGREDIENT in order['ingredients'] for order in response.json()['orders']))

    @allure.title('Тест получения заказа не авторизированным пользователем')
    def test_get_orders_non_authorized_user(self):
        helpers.create_order(TestData.INGREDIENT)
        response = helpers.get_user_orders()
        assert (response.status_code == 401 and
                response.json()['message'] == Message.SHOULD_BE_AUTHORISED_401)
