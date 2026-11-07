import psycopg
from getpass import getpass
from extract import extract_earthquakes
from transform import transform_earthquake
from load import load_earthquake

def main():
    raw_records = extract_earthquakes("data/raw/earthquakes.csv")
    clean_records = []
    rejected_count = 0

    for row in raw_records:
        result = transform_earthquake(row)
        
        if result is not None:
            clean_records.append(result)
        else:
            rejected_count += 1

    password = getpass("Database password: ")

    with psycopg.connect(
            host="127.0.0.1",
            port=5433,
            dbname="earthquake_db",
            user="analytics_user",
            password=password
    ) as connection:

        for earthquake in clean_records:
            load_earthquake(connection, earthquake)

    print("ETL pipeline completed!")
    print("Extracted:", len(raw_records))
    print("Accepted:", len(clean_records))
    print("Rejected:", rejected_count)

if __name__ == '__main__':
    main()