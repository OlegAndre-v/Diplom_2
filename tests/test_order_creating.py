import allure

import helpers
from data import TestData, Message


@allure.story('Тысты создания заказов')
class TestOrderCreating:
    @allure.title('Тест создания заказа с авторизацией')
    def test_order_creating_with_authorization(self, user):
        response = helpers.create_order(TestData.INGREDIENT, user['json']['accessToken'])
        assert response.status_code == 200 and response.json()['order']['owner']['email'] == user['email']

    @allure.title('Тест создания заказа')
    def test_order_creating(self):
        response = helpers.create_order(TestData.INGREDIENT)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Тест создания заказа без ингридиента')
    def test_order_creating_without_ingredient(self):
        response = helpers.create_order()
        assert (response.status_code == 400 and
                response.json()['message'] == Message.INGREDIENTS_MUST_BE_PROVIDED_400)

    @allure.title('Тест создания заказа с неверным хэшем')
    def test_order_creating_with_incorrect_hash(self):
        response = helpers.create_order('хэщ')
        assert response.status_code == 500
