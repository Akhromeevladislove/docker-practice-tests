import pytest
import requests
from health_check import check_website

# 1. Тест на доступность Google
def test_google_available():
    assert check_website("https://google.com") == True

# 2. Тест на публичное API (reqres.in)
def test_reqres_api():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"name": "John", "job": "QA Engineer"}
    
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John"
    assert response.json()["job"] == "QA Engineer"

# 3. Тест на недоступный сайт (должен упасть)
def test_unavailable_site():
    # Проверяем, что функция возвращает False для несуществующего сайта
    result = check_website("https://this-site-does-not-exist-12345.com")
    assert result == False

# 4. Тест на несколько сайтов
def test_multiple_sites():
    sites = [
        "https://google.com",
        "https://yandex.ru",
        "https://github.com"
    ]
    
    for site in sites:
        assert check_website(site) == True, f"Сайт {site} недоступен"