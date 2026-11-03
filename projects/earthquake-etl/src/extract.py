import csv
from pathlib import Path

def extract_earthquakes(_csv_path):

    csv_path = Path(_csv_path)

    with csv_path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        records = []

        for row in reader:
            records.append(row)

    return records

if __name__ == "__main__":
    records = extract_earthquakes("data/raw/earthquakes.csv")

    print("Total earthquakes:", len(records))
    print("First earthquake:", records[0]["id"])