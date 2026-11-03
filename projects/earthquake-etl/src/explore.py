import csv
from pathlib import Path

csv_path = Path("data/raw/earthquakes.csv")

with csv_path.open(newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    print(reader.fieldnames)
    
    count = 0
    for row in reader:
        if count < 3:
            print(row['id'],row['time'],row['mag'],row['place'])
        count+=1
    print(count)