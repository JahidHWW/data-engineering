import psycopg
from getpass import getpass

password = getpass("Database password: ")

with psycopg.connect(
    host="127.0.0.1",
    port=5433,
    dbname="earthquake_db",
    user="analytics_user",
    password=password
) as connection:
    print("Connected to PostgreSQL!")

    with connection.cursor() as cursor:
        cursor.execute('SELECT COUNT(*) FROM earthquakes;')

        result = cursor.fetchone()

        print(result[0])