import psycopg
from getpass import getpass


def load_earthquake(connection, earthquake):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO earthquakes (id, mag, depth, place)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING;
            """,
            (earthquake['id'],earthquake['mag'],earthquake['depth'],earthquake['place'])
        )

if __name__ == '__main__':
    password = getpass('Database password: ')

    with psycopg.connect(
        host='127.0.0.1',
        port=5433,
        dbname='earthquake_db',
        user='analytics_user',
        password=password
    ) as connection:
        print("Connected to PostgreSQL!")
        test_earthquake = {
            'id': 'test_load_003',
            'mag': 4.5,
            'depth': 12.3,
            'place': 'Alaska'
        }

        load_earthquake(connection, test_earthquake)
