import psycopg2

def get_value_from_db():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            database = "testdb",
            user = "testuser",
            password = "testpass",
        )
        cur = conn.cursor()
        cur.execute("SELECT VALUE FROM SystemSettings where name ilike 'clientname'")
        result = cur.fetchone()[0]

        # закрываем соединение
        cur.close()
        conn.close()
        return result
        
    except Exception as e:
        # Если подключение не устанавливается выводить ошибку
        print(f"❌ Ошибка подключения к PostgreSQL: {e}")

if __name__ == "__main__":
    print(f"Значение из БД = {get_value_from_db()}")