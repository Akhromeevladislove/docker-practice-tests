import psycopg2
import pytest

def test_postgress_connection():
    # Тест проверяет
    #1 Проверяет подключение
    #2 Проверка простого запроса
    #3 Возвращение результата
    
    try:
        #подключаемся к БД
        conn = psycopg2.connect(
            host = "localhost",
            database = "testdb",
            user = "testuser",
            password = "testpassword",
        )
        cur = conn.cursor()

        # выполняем запрос на получение данных из БД
        cur.execute("SELECT VALUE FROM SystemSettings where name ilike 'clientname'")
        result = cur.fetchone()[0]

        # закрываем соединение
        cur.close()
        conn.close()

        # проверяем результат
        assert result == 'test'
        print("✅ PostgreSQL работает корректно!")

    except Exception as e:
        # Если что-то пошло не так, то тест упадет
        pytest.fail(f"❌ Ошибка подключения к PostgreSQL: {e}")
    