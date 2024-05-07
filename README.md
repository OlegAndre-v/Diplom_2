## Дипломный проект. Задание 2: API-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы API-тесты, покрывающие ручки `/auth/register`, `/auth/user`, `/auth/login`, `/auth/user`, `/orders`


### Структура проекта

- `allure_results` - пакет, содержит allure отчет.
- `tests` - пакет, содержащий тесты, разделенные по ручкам.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание отчета**

>  `pytest tests --alluredir allure_results`

**Просмотр отчета в allure**

> `allure serve allure_results`
