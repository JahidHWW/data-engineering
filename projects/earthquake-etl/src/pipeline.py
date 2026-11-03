from extract import extract_earthquakes
from transform import transform_earthquake

raw_records = extract_earthquakes("data/raw/earthquakes.csv")

clean_records = []
rejected_count = 0

for row in raw_records:
    result = transform_earthquake(row)
    if result is not None:
        clean_records.append(result)
    else:
        rejected_count += 1

print("Extracted:", len(raw_records))
print("Accepted:", len(clean_records))
print("Rejected:", rejected_count)

invalid_row = {
    "id": "test123",
    "mag": "",
    "depth": "12.5",
    "place": "California"
}

result = transform_earthquake(invalid_row)

print("Invalid record result:", result)