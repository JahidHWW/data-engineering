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